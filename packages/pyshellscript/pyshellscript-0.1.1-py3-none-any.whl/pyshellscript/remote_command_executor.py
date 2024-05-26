import paramiko
import time
import select
from .utils import log


class SSHClient:
    def __init__(self, host, port, user, password, key_path, sudo_password, timeout=10, retry_interval=1):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_config = {
            "hostname": host,
            "port": port,
            "username": user,
            "key_filename": key_path,
            "password": password,
            "allow_agent": False,
            "look_for_keys": False,
            "timeout": timeout,
        }
        self.sudo_password = sudo_password
        self.connect(retry_interval, timeout)

    def connect(self, retry_interval, timeout):
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            try:
                self.client.connect(**self.ssh_config)
                log("SSH connection established.")
                break
            except paramiko.ssh_exception.NoValidConnectionsError as e:
                log(f"SSH transport is not ready. Retrying in {retry_interval} seconds... {e}")
                time.sleep(retry_interval)
            except Exception as e:
                log(f"Error connecting to SSH: {e}")

    def close(self):
        if self.client is not None:
            self.client.close()
            self.client = None

    def execute(self, command, streaming=False):
        """
        Execute a shell script on a remote server via SSH and optionally stream the output.
        :param script_path: Path to the local script to be executed.
        :param streaming: Flag to enable streaming of output.
        :param list_args: List of arguments to pass to the script.
        :return: A tuple containing lists of lines from stdout and stderr, and the exit code.
        """
        log(f"=== Executing on {self.ssh_config['hostname']}")
        stdin, stdout, stderr = self._prepare_execution(command)
        stdout_chunks, stderr_chunks = self._capture_output(stdout, stderr, streaming)
        exit_code = self._cleanup_and_exit(stdout, stderr)
        return stdout_chunks, stderr_chunks, exit_code

    def execute_script(self, script_path, streaming=False, list_args=None):
        """
        Execute a shell script on a remote server via SSH and optionally stream the output.
        :param script_path: Path to the local script to be executed.
        :param streaming: Flag to enable streaming of output.
        :param list_args: List of arguments to pass to the script.
        :return: A tuple containing lists of lines from stdout and stderr, and the exit code.
        """
        list_args = list_args or []
        log(f"=== Executing on {self.ssh_config['hostname']}")

        stdin, stdout, stderr = self._prepare_script_execution(list_args)
        self._send_script_content(script_path, stdout.channel)
        stdout_chunks, stderr_chunks = self._capture_output(stdout, stderr, streaming)
        exit_code = self._cleanup_and_exit(stdout, stderr)
        return stdout_chunks, stderr_chunks, exit_code

    def _prepare_execution(self, command):
        """
        Prepare the execution environment on the SSH client.
        :param list_args: List of arguments to pass to the script.
        :return: Tuple of stdin, stdout, stderr file-like objects.
        """
        command = f"sudo /bin/bash -c '{command}'"
        stdin, stdout, stderr = self.client.exec_command(command)
        channel = stdout.channel
        self._send_sudo_password(channel)
        return stdin, stdout, stderr

    def _prepare_script_execution(self, list_args):
        """
        Prepare the execution environment on the SSH client.
        :param list_args: List of arguments to pass to the script.
        :return: Tuple of stdin, stdout, stderr file-like objects.
        """
        command = f"sudo /bin/bash -s {' '.join(list_args)}"
        stdin, stdout, stderr = self.client.exec_command(command)
        channel = stdout.channel
        self._send_sudo_password(channel)
        return stdin, stdout, stderr

    def _send_sudo_password(self, channel):
        """
        Sends the sudo password if required.
        :param channel: Channel on which to send the password.
        """
        if self.sudo_password:
            while not channel.recv_ready():
                pass
            channel.send(self.sudo_password + '\n')

    def _send_script_content(self, script_path, channel):
        """
        Sends the script content to the channel.
        :param script_path: Path to the local script to be executed.
        :param channel: Channel to send the script content.
        """
        with open(script_path) as file:
            script_content = file.read()
        channel.send(str.encode(script_content))
        channel.shutdown_write()

    def _capture_output(self, stdout, stderr, streaming):
        """
        Captures output from stdout and stderr.
        :param stdout: Stdout file-like object.
        :param stderr: Stderr file-like object.
        :param streaming: Flag to enable streaming of output.
        :return: Tuple of lists containing stdout and stderr lines.
        """
        stdout_chunks, stderr_chunks = [], []
        while not stdout.channel.closed or stdout.channel.recv_ready() or stderr.channel.recv_stderr_ready():
            readq, _, _ = select.select([stdout.channel], [], [], 10)
            if not readq:
                break
            for recv in readq:
                if recv.recv_ready():
                    stdout_chunks += self._process_output(recv, stdout.channel, streaming)
                if recv.recv_stderr_ready():
                    stderr_chunks += self._process_output(recv, stderr.channel, streaming, stderr=True)
        return stdout_chunks, stderr_chunks

    def _process_output(self, recv, channel, streaming, stderr=False):
        """
        Process the output from a channel.
        :param recv: Receiver object.
        :param channel: Channel from which to read the output.
        :param streaming: Flag to enable streaming of output.
        :param stderr: Flag to indicate if the channel is for stderr.
        """
        output = channel.recv(len(recv.in_buffer)) if not stderr else channel.recv_stderr(len(recv.in_stderr_buffer))
        lines = output.decode("utf-8", "replace").strip("\n").splitlines()
        if streaming:
            for line in lines:
                log(line)
        return lines

    def _cleanup_and_exit(self, stdout, stderr):
        """
        Clean up the channels and get the exit status.
        :param stdout: Stdout file-like object.
        :param stderr: Stderr file-like object.
        :return: Exit status code.
        """
        stdout.close()
        stderr.close()
        exit_code = stdout.channel.recv_exit_status()
        if exit_code != 0:
            raise Exception("Command exited with code {}".format(exit_code))
        return exit_code
