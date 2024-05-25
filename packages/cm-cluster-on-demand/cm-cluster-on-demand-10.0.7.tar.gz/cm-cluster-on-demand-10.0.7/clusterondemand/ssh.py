#!/usr/bin/python
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
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import textwrap
import time
from io import TextIOWrapper
from typing import Any, Callable, Type

import paramiko
import tenacity
from paramiko import DSSKey, ECDSAKey, Ed25519Key, RSAKey

from clusterondemand import localpath
from clusterondemand.codoutput.sortingutils import SSHAlias
from clusterondemand.contextmanagers import SmartLock
from clusterondemand.exceptions import CODException
from clusterondemand.utils import (
    MAX_RFC3280_CN_LENGTH,
    is_valid_cluster_name,
    is_valid_ip_address,
    is_valid_positive_integer,
    is_writable_directory
)
from clusterondemandconfig import ConfigNamespace, config
from clusterondemandconfig.configuration_validation import must_be_nonnegative

clusterssh_ns = ConfigNamespace("cluster.ssh")

clusterssh_ns.add_parameter(
    "ssh_identity",
    advanced=True,
    default=None,
    help="Path to an ssh identity file key",
    help_varname="PATH_TO_FILE",
    parser=localpath.localpath,
    validation=[localpath.must_exist, localpath.must_be_readable]
)

clusterssh_ns.add_parameter(
    "ssh_password",
    advanced=True,
    default=None,
    help="SSH password to access the cluster",
    secret=True,
)

clusterssh_ns.add_parameter(
    "ssh_connect_timeout",
    advanced=True,
    default=30,
    help="Timeout for establishing an SSH connection with the cluster",
    validation=must_be_nonnegative,
)

clusterssh_ns.add_switch_parameter(
    "legacy_ssh_algo",
    advanced=True,
    help="Do not use rsa-sha2-512 and rsa-sha2-256 for SSH key verification",
)

log = logging.getLogger("cluster-on-demand")

# Suppress paramiko's logging
logging.getLogger("paramiko").setLevel(logging.WARNING)
# Suppress ERROR: Unknown exception: q must be exactly 160, 224, or 256 bits long
# https://jira.brightcomputing.com:8443/browse/CM-49054
logging.getLogger("paramiko.transport").disabled = True


class SSHConfigManagerException(Exception):
    """SSH configuration manager specific exceptions base class."""
    pass


class MultipleCodTypesException(Exception):
    """"""
    pass


# ssh directives (cf. man ssh_config)
HOST_ = "Host "
HOSTNAME_ = "HostName "


class SSHConfigHostDescriptor:
    """
    :param host: the host name, must be a valid cluster name.
    :param index: the index used to build the alias.
    :param prefix: the prefix used to build the alias.
    :param ip: the host IP, must be a valid IPv4 address.
    """
    # Notice: this ctor does not perform any validation. This is intentional, the instance owner must
    # always check the `is_valid` property to decide whether the instance should be used or discarded.
    def __init__(self, host: str | None, index: int | None, prefix: str, ip: str | None) -> None:
        self._host = host
        self._index = index
        self._prefix = prefix
        self._ip = ip

    @property
    def is_valid(self) -> bool:
        return (is_valid_cluster_name(self.host, MAX_RFC3280_CN_LENGTH) and
                is_valid_ip_address(self.ip) and
                is_valid_positive_integer(self.index))

    @property
    def host(self) -> str | None:
        return self._host

    @property
    def index(self) -> int | None:
        return self._index

    @property
    def ip(self) -> str | None:
        return self._ip

    @property
    def alias(self) -> str:
        return "{prefix}{index}".format(
            prefix=self._prefix,
            index=self._index
        )

    @staticmethod
    def from_lines(lines: list[str], prefix: str) -> SSHConfigHostDescriptor:
        host, index, ip = (None, ) * 3
        try:
            for line in (li.strip() for li in lines):
                if line.startswith(HOST_):
                    line = line.replace(HOST_, "").strip()

                    tmp = line.split(" ")
                    host = tmp[0]
                    index = int(tmp[1].replace(prefix, ""))

                elif line.startswith(HOSTNAME_):
                    line = line.replace(HOSTNAME_, "").strip()
                    ip = line.split(" ")[0]
        except Exception:
            pass  # silence errors

        return SSHConfigHostDescriptor(host, index, prefix, ip)

    def __str__(self) -> str:
        return textwrap.dedent("""
        Host {host} {alias}
            HostName {ip}
            User root
            UserKnownHostsFile /dev/null
            StrictHostKeyChecking=no
            CheckHostIP=no
            LogLevel=error""".format(host=self.host, alias=self.alias, ip=self.ip))


class SSHConfigManager:
    """
    A helper class to manage cluster-related entries in local ssh_config file.

    :param cod_type: the type of cod clusters to be managed, i.e os or vmware.
    :param ssh_config: the path of the local ssh configuration file to use.
    :param prefix: the prefix used to build the cluster ssh aliases.
    :param parse: enable parsing the contents of the ssh_config file.
    :param mode: Either "match-hosts" or "replace-hosts". "match-hosts" preserves the contents of the
                 COD section or the ssh_config file; "replace-hosts" ignores currently defined hosts.
                 User-defined contents are always preserved.
    """
    def __init__(self, cod_type: str, ssh_config: str = "~/.ssh/config", prefix: str = "", parse: bool = True,
                 mode: str = "match-hosts") -> None:

        # params
        self._ssh_config = os.path.expanduser(ssh_config)
        self._prefix = prefix
        if mode not in ["match-hosts", "replace-hosts"]:
            raise SSHConfigManagerException("Programming error")
        self._mode = mode

        # internals
        self._begin_marker = f"#### BEGIN COD-{cod_type.upper()} SECTION"
        self._end_marker = f"#### END COD-{cod_type.upper()} SECTION"
        self._cod_type = cod_type
        self._hosts: list[SSHConfigHostDescriptor] = []
        self._cod_section: list[str] = []
        self._usr_section: list[str] = []

        self._parsed = False
        self._changed = False

        # disabling parsing of the local ssh config can be useful if the configuration is actually broken
        if parse:
            if not os.path.exists(self._ssh_config):
                # Non-existing config file is equivalent to empty config file
                log.warning("File '%s' was not found, continuing with an empty configuration.",
                            self._ssh_config)
                self._parsed = True
            else:
                try:
                    with open(self._ssh_config) as config:
                        self._parse_config(config)
                        self._parsed = True

                except OSError as ioe:
                    log.warning(str(ioe))

    @staticmethod
    def lock(ssh_config: str = "~/.ssh/config") -> Any:
        return SmartLock(os.path.expanduser(ssh_config) + ".lock")

    def _check_parsed(self) -> None:
        if not self._parsed:
            raise SSHConfigManagerException(
                "File '%s' not successfully parsed",
                self._ssh_config
            )

    @property
    def hosts(self) -> list[SSHConfigHostDescriptor]:
        """A list of host descriptors"""
        self._check_parsed()
        return self._hosts

    @property
    def user(self) -> list[str]:
        """Contents of the user section"""
        self._check_parsed()
        return self._usr_section

    def add_host(self, host: str, ip: str, override: bool = False) -> SSHConfigHostDescriptor:
        """
        Add a host descriptor to current configuration. Invalid descriptors are discarded.

        :param host: the hostname (string)
        :param ip: the host IPv4 or IPv6 address (string)
        :param override: (reserved for cluster create) if another host with the same name already exists, remove the
        the corresponding entry before adding this host. If override is False, trying to add an already existing host
        will raise an exception.

        :return: the host descriptor that has been added.
        """
        self._check_parsed()

        exists = next((h for h in self._hosts if h.host == host), None)
        if exists:
            if override:
                log.warning("Replacing local ssh config entry for host '%s'", host)
                self.remove_host(host)
            else:
                raise SSHConfigManagerException("A descriptor already exists for host '%s'" % host)

        next_index = max(h.index for h in self._hosts if h.index) + 1 if self._hosts else 1

        res = SSHConfigHostDescriptor(host, next_index, self._prefix, ip)
        self._safe_add_host_descriptor(res)

        return res

    def remove_host(self, host: str) -> None:
        """
        Remove a host descriptor from current configuration

        :param host: the hostname (string)
        """
        self._check_parsed()
        prev_hosts = self._hosts
        self._hosts = [h for h in prev_hosts if h.host != host]
        if self._hosts != prev_hosts:
            self._changed = True
        else:
            log.debug(
                "host descriptor for '%s' could not be found.", host)

    def write_configuration(self) -> None:
        """
        Write configuration to ssh config file.

        SSH clients give higher priority to entries towards the top of the config
        files. Therefore the COD section is put at the head of the local ssh config
        file. If no hosts are defined (i.e. no clusters), the section will be omitted.
        """
        msg = "cowardly refusing to write file '{ssh_config}'!".format(
            ssh_config=self._ssh_config
        )

        if not self._parsed:
            log.debug("%s (file was not parsed).", msg)
            return

        if not self._changed:
            log.debug("%s (no changes detected).", msg)
            return

        if not is_writable_directory(os.path.dirname(self._ssh_config)):
            log.debug("%s (directory is not writable).", msg)
            return

        assert self._parsed and self._changed
        log.debug("rewriting local ssh config file '%s' with %d COD %s.",
                  self._ssh_config, len(self._hosts),
                  "entry" if 1 == len(self._hosts) else "entries")

        try:
            # we go the extra mile of writing the new config to a temp file and only when we known
            # everything went smooth, we overwrite the pre-existing file by copying the new one onto it.

            with tempfile.NamedTemporaryFile(mode="wt") as fd:
                # Write COD section
                if self._hosts:
                    fd.write(self._begin_marker)
                    fd.write(textwrap.dedent(f"""
                    #### NOTICE: This section of the file is managed by cm-cod-{self._cod_type}. Manual changes to this section will be
                    #### overwritten next time cm-cod-{self._cod_type} cluster create, delete or list --update-ssh-config is executed."""))  # noqa

                    for descr in self._hosts:
                        # no point in keeping invalid entries here
                        if not descr.is_valid:
                            log.debug("Skipping invalid host descriptor for '%s'",
                                      descr.host or "?")
                            continue

                        fd.write(str(descr))
                        fd.write("\n")

                    fd.write(self._end_marker)
                    fd.write("\n")

                # Dump non-COD config as-is
                for line in self._usr_section:
                    fd.write(line)
                fd.flush()

                shutil.copy(fd.name, self._ssh_config)

                # issue warning if preservation of user contents semantics can not be guaranteed: we look for a
                # Host * directive, at the top of the ssh config file. If COD section exists and if this directive
                # can not be found, a warning is issued.
                if self._usr_section and self._hosts:
                    try:
                        if not re.match(r"%s\s+\*" % HOST_.lower().strip(),
                                        next(i for i in (i.strip() for i in self._usr_section if i.strip())
                                             if not i.startswith("#")).lower()):
                            log.warning(
                                "Possibly unsafe changes were made to '{config}'. To avoid this "
                                "warning, please add a 'Host *' directive right after the end of the "
                                "COD section.".format(
                                    config=self._ssh_config
                                ))
                    except StopIteration:
                        pass

        except OSError as ioe:
            log.warning("Could not write file '%s' (%s).", self._ssh_config, str(ioe))

    def get_host_index(self, host_name: str) -> int | None:
        try:
            return next(host.index for host in self._hosts if host.host == host_name)
        except StopIteration:
            raise SSHConfigManagerException(f"{host_name} not found in ssh config")

    def get_host_alias(self, host_name: str) -> SSHAlias:

        try:
            alias_string = next(host.alias for host in self._hosts if host.host == host_name)
            return SSHAlias(alias_string, self._prefix)
        except StopIteration:
            raise SSHConfigManagerException(f"{host_name} not found in ssh config")

    def _safe_add_host_descriptor(self, descriptor: SSHConfigHostDescriptor) -> None:
        """
        If a  valid descriptor is given, add it to the internal cache. Otherwise discard it.

        :param descriptor: An instance of class SSHConfigHostDescriptor
        """
        if descriptor.is_valid:
            self._hosts.append(descriptor)
            self._changed = True
            log.debug("added host descriptor for '%s'", descriptor.host)
        else:
            log.debug("discarding not well-formed descriptor for host '%s'",
                      descriptor.host or "?")

    def _parse_config(self, fd: TextIOWrapper) -> None:
        """
        Parse ssh config file.

        :param fd: An open file descriptor

        The ssh config file is logically divided in two sections: the COD section contains
        all host definitions for COD clusters, along with an alias than can be used with ssh
        -like tools, and the IP to reach the head-node and a few configuration options. It is
        enclosed between the begin and end markers; the other section (i.e. anything beyond
        the COD section) is reserved to the user and is preserved as-is.
        """
        if self._mode == "match-hosts":
            self._parse_config_aux(fd)

        elif self._mode == "replace-hosts":
            self._parse_config_aux(fd)
            log.debug("regenerating contents of {config}".format(
                config=self._ssh_config
            ))
            self._hosts = []
            self._changed = True

        else:
            assert False

    def _parse_config_aux(self, fd: TextIOWrapper) -> None:
        in_cod_section = False
        for line in fd:
            if line.startswith(self._begin_marker):
                if in_cod_section:
                    raise SSHConfigManagerException(
                        "Unexpected begin marker encountered")
                in_cod_section = True
                continue

            if line.startswith(self._end_marker):
                if not in_cod_section:
                    raise SSHConfigManagerException(
                        "Unexpected end marker encountered")
                in_cod_section = False
                continue

            if line.startswith("#### BEGIN") and not self._prefix:
                raise MultipleCodTypesException()

            if in_cod_section and line.startswith("####"):  # skip markers in COD section
                continue

            # every line goes either to the COD section or the user section
            section = self._cod_section if in_cod_section else self._usr_section
            section.append(line)

        # at EOF we're supposed to be out of the COD section
        if in_cod_section:
            raise SSHConfigManagerException(
                "Missing end marker detected")

        # This loop maintains in 'curr' a list of lines. We scan the entire file, line by line, accumulating
        # lines in 'curr'. Every time we encounter a Host declaration we want to process the accumulated lines.
        # Then, we reset the 'curr' list and continue. Once we've scanned the entire file, a few lines will
        # still be in curr. Those will be processed separately.
        curr: list[str] = []
        for line in self._cod_section:
            # "Match" is not supported within the COD section
            if line.startswith(HOST_):
                if curr:
                    descriptor = SSHConfigHostDescriptor.from_lines(lines=curr, prefix=self._prefix)
                    self._safe_add_host_descriptor(descriptor)
                    curr = []
            curr.append(line)

        # final wrap-up
        if curr:
            descriptor = SSHConfigHostDescriptor.from_lines(lines=curr, prefix=self._prefix)
            self._safe_add_host_descriptor(descriptor)
            curr = []

        assert not curr, "Unexpected"
        log.debug(
            "local ssh config file '%s' parsed, COD section holds %d %s.",
            self._ssh_config, len(self._hosts),
            "entry" if 1 == len(self._hosts) else "entries")


def private_key_for_public(public_key_path: str) -> str | None:
    if not public_key_path:
        return None

    name, ext = os.path.splitext(public_key_path)
    if os.path.exists(name) and ext:
        return name

    return None


def validate_ssh_access(floating_ip: str, port: int | None = None) -> None:
    try:
        with SSHExecutor(floating_ip, port=port):
            pass
    except SSHAuthenticationError as e:
        raise CODException(textwrap.dedent(f"""
        Authentication error while connecting to root@{floating_ip}. Make sure that provided
        credentials are valid or that you have a valid passwordless SSH access to the cluster.
        Consider using --ssh-identity and/or --ssh-password parameters or using SSH Agent
        with added corresponding identity (recommended).
        If you're creating a cluster check the following options:
        --ssh-key-pair, --ssh-pub-key-path and --ssh-password-authentication.
        """), e)


class SSHExecutorError(Exception):
    pass


class SSHTimeoutError(SSHExecutorError):
    def __init__(self, host: str, command: str, stdout: bytes, stderr: bytes, timeout: float) -> None:
        self.host = host
        self.command = command
        self.stdout = stdout
        self.stderr = stderr
        self.timeout = timeout
        self.message = (f"Command '{self.command}' on the host {self.host} wasn't"
                        f" exited in {self.timeout} seconds")
        super().__init__(self.message)


class SSHAuthenticationError(SSHExecutorError):
    def __init__(self, host: str) -> None:
        self.host = host
        self.message = f"Failed to connect to the host {self.host}: authentication error"
        super().__init__(self.message)


class SSHConnectionError(SSHExecutorError):
    def __init__(self, host: str) -> None:
        self.host = host
        self.message = f"Failed to connect to the host {self.host}: connection error"
        super().__init__(self.message)


class SSHExecutor:
    """
    A utility class to interact with a cluster head node via SSH

    :param host: the host (or IP) of the head node
    :param user: the SSH user. If None (default) is used, user `root` will be used
    :param identity_files: the SSH identity files
    :param password: the SSH password
    :param raise_exceptions: If false it returns exit status wherever possible instead of
                             raising exceptions. It's needed for old code only
    :param connect_timeout: number of seconds to retry establishing a connection to the SSH server
    :param wait_between_connect_retries: number of seconds to wait between connection retries
    """

    def __init__(self, host: str, user: str | None = None, identity_file: str | None = None,
                 password: str | None = None, raise_exceptions: bool = True,
                 connect_timeout: float | int | None = None, wait_between_connect_retries: float = 10,
                 port: int | None = None) -> None:
        if identity_file is None:
            identity_file = config.get("ssh_identity")
        if identity_file is None:
            identity_file = private_key_for_public(config.get("ssh_pub_key_path"))
        if password is None:
            password = config.get("ssh_password")
        if password is None:
            password = config.get("cluster_password")
        if connect_timeout is None:
            connect_timeout = config.get("ssh_connect_timeout")

        # if some command makes use of this class but forgets to import --ssh-connect-timeout,
        # this will lead to unclear errors.
        assert isinstance(connect_timeout, (int, float)) and connect_timeout >= 0, "timeout must be positive number"

        self._host: str = host
        self._port: int = port or 22
        self._user = user or "root"
        self._identity_file = identity_file
        self._password = password
        self._raise_exceptions = raise_exceptions
        self._keep_connection = False
        self._ssh_client: paramiko.SSHClient | None = None
        self._last_error: Exception | None = None
        self._connect_timeout = connect_timeout
        self._wait_between_connect_retries = wait_between_connect_retries

        if config.get("legacy_ssh_algo", None):
            self._disabled_algos = {"pubkeys": ["rsa-sha2-256", "rsa-sha2-512"]}
        else:
            self._disabled_algos = {}

    def __enter__(self) -> SSHExecutor:
        self._connect()
        self._keep_connection = True
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self._keep_connection = False
        self._close()

    @property
    def last_error(self) -> Exception | None:
        """ Get last error raised by ssh client """
        return self._last_error

    def get_ssh_client(self) -> paramiko.SSHClient | None:
        """ Get underlying SSH client. Must be called only inside of the 'with' statement """
        assert self._keep_connection
        return self._ssh_client

    def _close(self) -> None:
        if self._ssh_client:
            self._ssh_client.close()
            self._ssh_client = None

    def _try_connect_using_ssh_client(self) -> None:
        # This is a small optimization to cache passphrases in SSH Agent and avoid
        # paramiko's bug with asking a passpharse for each private key
        args = [
            "ssh", "-q",
            "-o", "PasswordAuthentication=no",
            "-o", "StrictHostKeyChecking=no",
            "-o", "UserKnownHostsFile=/dev/null",
            "-o", "ConnectTimeout=1",
            "-o", "BatchMode=yes",  # Avoid stucks because of waiting for keyboard input
            f"{self._user}@{self._host}",
            "exit"
        ]
        try:
            subprocess.check_call(args)
        except subprocess.CalledProcessError as e:
            # This is probably not an error, maybe password auth will work
            # Caller will handle connection/auth errors itself
            log.debug("Authentication using SSH client failed: %s", e)
        else:
            log.debug("Authentication using SSH client was successful")

    def _connect(self) -> None:
        if self._ssh_client:
            return

        self._try_connect_using_ssh_client()

        assert self._ssh_client is None
        self._ssh_client = paramiko.SSHClient()
        self._ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        connected = False

        @tenacity.retry(
            stop=tenacity.stop_after_delay(self._connect_timeout),
            wait=tenacity.wait_fixed(self._wait_between_connect_retries),
            before_sleep=tenacity.before_sleep_log(log, logging.DEBUG),
            reraise=True,
        )
        def connect_wait(ssh_client: paramiko.SSHClient) -> None:
            # The host key may change during the booting process, so refresh previously saved key
            if self._host in ssh_client.get_host_keys():
                del ssh_client.get_host_keys()[self._host]

            # TODO(kal): Fix paramiko upstream or migrate.
            if self._identity_file is not None:
                for pkey_class in (RSAKey, Ed25519Key, DSSKey, ECDSAKey):
                    try:
                        pkey = None
                        try:
                            pkey = pkey_class.from_private_key_file(self._identity_file)  # type: ignore
                        except Exception:
                            # from_private_key_file() will fail if the key file is encrypted.
                            # Call connect() anyway in case the key is available through an agent.
                            pass
                        ssh_client.connect(
                            self._host,
                            port=self._port,
                            username=self._user,
                            pkey=pkey,
                            password=self._password,
                            disabled_algorithms=self._disabled_algos,
                            timeout=self._wait_between_connect_retries,
                        )
                        return
                    except Exception as e:
                        # connect() may fail until we try the correct key class.
                        error = e
                raise error

            ssh_client.connect(
                self._host,
                port=self._port,
                username=self._user,
                password=self._password,
                disabled_algorithms=self._disabled_algos,
                timeout=self._wait_between_connect_retries,
                allow_agent=False,
            )

        try:
            log.debug(f"Creating an SSH connection to {self._user}@{self._host} (timeout {self._connect_timeout}s)")
            connect_wait(self._ssh_client)
            connected = True
            log.debug(f"SSH connection to {self._user}@{self._host} established")
        except paramiko.AuthenticationException as e:
            self._last_error = e
            raise SSHAuthenticationError(self._host) from e
        except Exception as e:
            self._last_error = e
            raise SSHConnectionError(self._host) from e
        finally:
            if not connected:
                self._ssh_client = None

    def _print_call(self, print_func: Callable[..., None],
                    command: str | list[str], status: int, out: bytes, err: bytes) -> None:
        print_func("SSH command '%s' returned status %s.%s%s", command, status,
                   f" Remote STDOUT: {out[:4096]!r}." if out else "",
                   f" Remote STDERR: {err[:4096]!r}." if err else "")

    def run(self, command: str | list[str], timeout: float = 1800, max_stdout_size: int = 100 * 2**20,
            max_stderr_size: int = 100 * 2**20, capture_out: bool = False,
            capture_err: bool = False) -> tuple[int, bytes, bytes]:
        if isinstance(command, list):
            command = " ".join(shlex.quote(arg) for arg in command)

        stdin, stdout, stderr, channel = None, None, None, None
        out_chunks, err_chunks = [], []
        try:
            self._connect()
            stdin, stdout, stderr = self._ssh_client.exec_command(command)  # type: ignore
            channel = stdin.channel  # Channel is the same for stdin/stdout/stderr

            # Close write as we don't have any input
            channel.shutdown_write()

            out_size, err_size = 0, 0
            timed_out = False
            end_time = time.monotonic() + timeout
            while time.monotonic() < end_time:
                if channel.recv_ready():
                    if capture_out and out_size < max_stdout_size:
                        chunk = channel.recv(max_stdout_size - out_size)
                        out_size += len(chunk)
                        out_chunks.append(chunk)
                    else:
                        chunk = channel.recv(2**20)
                        if not capture_out:
                            sys.stdout.write(chunk.decode("utf-8", errors="replace"))
                        else:
                            pass  # Consume but do nothing to avoid blocking the command
                if channel.recv_stderr_ready():
                    if capture_err and err_size < max_stderr_size:
                        chunk = channel.recv_stderr(max_stderr_size - err_size)
                        err_size += len(chunk)
                        err_chunks.append(chunk)
                    else:
                        chunk = channel.recv_stderr(2**20)
                        if not capture_err:
                            sys.stderr.write(chunk.decode("utf-8", errors="replace"))
                        else:
                            pass  # Consume but do nothing to avoid blocking the command
                if channel.closed or channel.exit_status_ready():
                    break
                time.sleep(0.01)
            else:
                timed_out = True

            out = b"".join(out_chunks)
            err = b"".join(err_chunks)
            status = channel.recv_exit_status() if not timed_out else 255

            if status != 0:
                if status not in range(256):
                    log.debug("recv_exit_status returned unexpected status value: %d."
                              " It will be replaced by 255", status)
                    status = 255
                self._print_call(log.debug, command, status, out, err)

            if timed_out:
                raise SSHTimeoutError(self._host, command, out, err, timeout)

            return status, out, err
        except SSHTimeoutError as e:
            log.debug("SSH command timed out: %s", e)
            if not self._raise_exceptions:
                return 255, e.stdout, e.stderr
            raise
        except Exception as e:
            log.debug("Failed to execute SSH command '%s': %s", command, e)
            self._last_error = e
            if not self._raise_exceptions:
                return 255, b"", b""
            raise
        finally:
            if stdin is not None:
                stdin.channel.close()
                stdin.close()
            if stdout is not None:
                stdout.close()
            if stderr is not None:
                stderr.close()
            if not self._keep_connection:
                self._close()

    def print_error(self, error: Type[Exception]) -> None:
        if isinstance(error, subprocess.CalledProcessError):
            self._print_call(log.error, error.cmd, error.returncode, error.output, error.stderr)

    def call(self, command: str | list[str], **run_kwargs: Any) -> int:
        return self.run(command, **run_kwargs)[0]

    # Consistent with subprocess.check_call, do not print error here
    def check_call(self, command: str | list[str], **run_kwargs: Any) -> None:
        status, stdout, stderr = self.run(command, **run_kwargs)
        if status != 0:
            raise subprocess.CalledProcessError(status, command, output=stdout, stderr=stderr)

    # Consistent with subprocess.check_output, do not print eror here
    def check_output(self, command: str | list[str], **run_kwargs: Any) -> bytes:
        status, stdout, stderr = self.run(command, capture_out=True, **run_kwargs)
        if status != 0:
            raise subprocess.CalledProcessError(status, command, output=stdout, stderr=stderr)
        return stdout

    def scp_to_remote(self, src: str, dst: str, preserve_perms: bool = False) -> int:
        try:
            self._connect()
            with self._ssh_client.open_sftp() as sftp:  # type: ignore
                sftp.put(src, dst)
                if preserve_perms:
                    stat = os.stat(src)
                    sftp.chmod(dst, stat.st_mode)
                    sftp.utime(dst, (stat.st_atime, stat.st_mtime))
            return 0
        except SSHExecutorError as e:
            log.debug("SCP to %s failed: %s", dst, e)
            self._last_error = e
            if not self._raise_exceptions:
                return 255
            raise
        except Exception as e:
            log.debug("SCP to %s failed: %s", dst, e)
            self._last_error = e
            if not self._raise_exceptions:
                return 1
            raise
        finally:
            if not self._keep_connection:
                self._close()

    def scp_from_remote(self, src: str, dst: str) -> int:
        try:
            self._connect()
            with self._ssh_client.open_sftp() as sftp:  # type: ignore
                sftp.get(src, dst)
            return 0
        except SSHExecutorError as e:
            log.debug("SCP from %s failed: %s", src, e)
            self._last_error = e
            if not self._raise_exceptions:
                return 255
            raise
        except Exception as e:
            log.debug("SCP from %s failed: %s", src, e)
            self._last_error = e
            if not self._raise_exceptions:
                return 1
            raise
        finally:
            if not self._keep_connection:
                self._close()

    def scp_and_call(self, script_path: str) -> bool:
        if self.scp_to_remote(script_path, "/tmp/caas-script"):
            log.error("Failed to scp %s to %s." % (script_path, self._host))
            return False

        if self.call("chmod 700 /tmp/caas-script && /tmp/caas-script && rm /tmp/caas-script"):
            log.error("Failed to run %s on %s." % (script_path, self._host))
            return False

        return True

    def scp_and_call_on_chroot(self, script_path: str, root: str) -> bool:
        temp_script = "tmp/caas-script"
        dest_path = os.path.join(root, temp_script)

        if self.scp_to_remote(script_path, dest_path):
            log.error("Failed to scp %s to %s." % (script_path, self._host))
            return False

        cmd = "chroot {root} /bin/bash -c 'chmod 700 {script} && {script} && rm {script}'".format(
            root=root, script=os.path.join("/", temp_script))
        if self.call(cmd):
            log.error("Failed to run %s on %s." % (script_path, self._host))
            return False

        return True
