# Copyright 2004-2024 Bright Computing Holding BV
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import logging
import time
from collections.abc import Collection
from typing import Any

import tenacity

from clusterondemand.bcm_version import BcmVersion
from clusterondemand.configuration_validation import is_ssh_key_specified
from clusterondemand.const import BASIC_SERVICES
from clusterondemand.exceptions import CODException
from clusterondemand.ssh import SSHAuthenticationError, SSHConnectionError, SSHExecutor, validate_ssh_access
from clusterondemandconfig import ConfigNamespace
from clusterondemandconfig.configuration import ConfigurationView, MutableConfigurationView
from clusterondemandconfig.exceptions import ConfigLoadError

from .cmclient import CMDaemonJSONClient
from .utils import wait_for_socket

log = logging.getLogger("cluster-on-demand")

clusterwaiters_ns = ConfigNamespace("cluster.waiters")
clusterwaiters_ns.add_parameter(
    "wait_ssh",
    default=300,
    help_varname="SECONDS",
    help="Wait up to that many seconds for SSH to come up"
)
clusterwaiters_ns.add_parameter(
    "wait_cmdaemon",
    default=600,
    help_varname="SECONDS",
    help="Wait up to that many seconds for CMDaemon to come up"
)
clusterwaiters_ns.add_switch_parameter(
    "start_nodes",
    default=False,
    help="Power on compute nodes after starting the cluster"
)
clusterwaiters_ns.add_parameter(
    "wait_for_nodes",
    default=0,
    help_varname="SECONDS",
    help="Wait for up to that many seconds for the compute nodes to come up"
)
clusterwaiters_ns.add_validation(lambda param, config: validate_waiters(config))


def wait_for_ssh(floating_ip: str, timeout: float) -> None:
    log.info("Waiting for sshd to start (ssh root@%s)." % floating_ip)
    wait_for_socket(floating_ip, 22, timeout, throw=True)

    log.debug(f"Waiting for {timeout:.0f} seconds.")
    try:
        with SSHExecutor(floating_ip, connect_timeout=timeout):
            pass
    except SSHConnectionError:
        raise CODException(f"Timed out while waiting for sshd to start (ssh root@{floating_ip}).")
    except SSHAuthenticationError:
        # SSHd started successfully. Caller should use validate_ssh_access function to check access
        pass
    log.debug("sshd initialized. Finished waiting.")
    return


def wait_for_cmdaemon_to_start(floating_ip: str, timeout: float, cmdaemon_version: str | None = None,
                               only_sock: bool = False) -> CMDaemonJSONClient | None:
    log.info("Waiting for CMDaemon to start.")
    wait_for_socket(floating_ip, 8081, timeout, throw=True)
    if only_sock:
        return None

    client = CMDaemonJSONClient(floating_ip, cmdaemon_version=cmdaemon_version)
    ready_call_timeout = 10

    timed_out_msg = "Timed out while waiting for CMDaemon to initialize."

    @tenacity.retry(
        stop=tenacity.stop_after_delay(timeout),
        retry=tenacity.retry_if_exception_message(timed_out_msg),
        wait=tenacity.wait_fixed(1),
        before_sleep=tenacity.before_sleep_log(log, logging.DEBUG),
        reraise=True,
    )
    def client_wait() -> None:
        services = BASIC_SERVICES
        if not client.ready(ready_call_timeout, services=services):
            raise CODException(timed_out_msg)

    log.info("Waiting for CMDaemon to initialize.")
    client_wait()
    log.debug("CMDaemon initialized. Finished waiting.")
    return client


def wait_for_compute_nodes(cmclient: CMDaemonJSONClient, timeout: float,
                           node_names: Collection[str] | None = None) -> None:
    try:
        nodes = {n[cmclient.entity_unique_field_name]: n for n in cmclient.getComputeNodes()
                 if node_names is None or n["hostname"] in node_names}
    except Exception as e:
        raise Exception("Failed to get compute nodes" +
                        (f" {node_names} " if node_names else " ") +
                        "to wait for") from e

    if not nodes:
        log.debug("No compute nodes to wait for")
        return

    log.info(f"Waiting for compute nodes {[n['hostname'] for n in nodes.values()]} to start.")

    if BcmVersion(cmclient.call("cmmain", "getVersion")["cmVersion"]) > "8.2":
        log.debug("Using new device status API to wait for nodes.")
        api_service = "cmstatus"
        api_method = "getStatusForDevices"
    else:
        log.debug("Using old device status API to wait for nodes.")
        api_service = "cmdevice"
        api_method = "getStatusForDeviceArray"

    if cmclient.need_uuid:
        node_keys = list(nodes.keys())
    else:
        node_keys = [int(k) for k in nodes.keys()]

    remaining_nodes: list[dict[str, Any]] = list(nodes.values())
    end_time = time.time() + timeout
    while time.time() < end_time:
        log.debug("Fetching node status from CMDaemon.")
        statuses = cmclient.call(api_service, api_method, [node_keys])

        remaining_nodes = []
        stopped_nodes = []
        for status in statuses:
            node = nodes[status[cmclient.ref_device_field_name]]
            status_name = status["status"]
            log.debug(f"Node {node['hostname']} is {status_name}")
            if status_name != "UP":
                remaining_nodes.append(node)
            if status_name == "DOWN":
                stopped_nodes.append(node)

        if stopped_nodes:
            try:
                log.debug("Some compute nodes became DOWN during powering on, let's try to power"
                          " them on again...")
                cmclient.powerOnNodes(stopped_nodes)
            except Exception:
                log.debug("Failed while retrying power on, probably because previous power on "
                          " operation is still running", exc_info=True)

        if not remaining_nodes:
            break

        remaining_time = end_time - time.time()
        if remaining_time > 0:
            log.debug("Waiting for %d of %d nodes to start, %d:%02d min remaining...",
                      len(remaining_nodes), len(nodes), remaining_time // 60, remaining_time % 60)
            time.sleep(min(10, remaining_time))
    else:
        names = [n["hostname"] for n in remaining_nodes]
        raise CODException(f"Timed out while waiting for nodes {names} to start")


def wait_for_cluster_to_be_ready(config: ConfigurationView, floating_ip: str, bcm_version: str) -> None:
    if config["wait_ssh"] > 0:
        wait_for_ssh(floating_ip, config["wait_ssh"])
    else:
        log.info("Not waiting for SSH")

    if config["wait_cmdaemon"] > 0:
        if config["wait_ssh"] > 0:
            validate_ssh_access(floating_ip)
            cmclient = wait_for_cmdaemon_to_start(floating_ip, config["wait_cmdaemon"], bcm_version)
        else:
            # Without SSH access we are not able to download CMDaemon creds to connect to it
            # and wait until it starts properly. So, let's wait until its socket at least.
            wait_for_cmdaemon_to_start(floating_ip, config["wait_cmdaemon"], only_sock=True)

    if config["start_nodes"]:
        assert cmclient, "Use validate_waiters to validate these params"
        cmclient.powerOnNodes(cmclient.getComputeNodes())

    if config["wait_for_nodes"] > 0:
        assert cmclient and config["start_nodes"], "Use validate_waiters to validate these params"
        wait_for_compute_nodes(cmclient, config["wait_for_nodes"])


def validate_waiters(config: MutableConfigurationView) -> None:
    # Not all configuration parameters are used for all "cod" commands, but some of those commands still need waiters
    # Therefore, we  validate the values of various keys, only if those keys exist in configuration
    if not config.get("run_cm_bright_setup", True) and (config["wait_cmdaemon"] or config["wait_for_nodes"]):
        log.warning("--run-cm-bright-setup=no overrides --wait-cmdaemon and --wait-for-nodes options")
        config["wait_cmdaemon"] = 0
        config["wait_for_nodes"] = 0
    if config["wait_for_nodes"] > 0:
        if ("ssh_key_pair" in config or "ssh_pub_key_path" in config) and not is_ssh_key_specified(config):
            raise ConfigLoadError("Using '--wait-for-nodes' requires path to ssh key to be specified")
        if "wait_cmdaemon" in config and not config["wait_cmdaemon"] > 0:
            raise ConfigLoadError("Using '--wait-for-nodes' requires '--wait-cmdaemon' to also be set")
        if "start_nodes" in config and not config["start_nodes"]:
            raise ConfigLoadError("Using '--wait-for-nodes' requires '--start-nodes' to also be set")
