import subprocess
from .utils import log, escape_ansi


def run_shell_command(command, streaming=False):
    """
    Run a shell command and optionally stream the output.

    Args:
        command (str): The command to execute in the shell.
        streaming (bool, optional): If True, live stream the output. Defaults to False.

    Returns:
        tuple: A tuple containing the stdout, stderr, and exit status code of the command.
    """
    try:
        log(f"Executing command: {command}")
        # Ensure commands are properly tokenized, especially if args contain spaces.
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if streaming:
            stdout_lines = []
            # Stream output line by line
            for line in process.stdout:
                stripped_line = line.strip()
                log(">>", stripped_line)
                stdout_lines.append(escape_ansi(stripped_line))
            out, err = process.communicate()
            # Collect any remaining output if process has already finished
            stdout_complete = "\n".join(stdout_lines)
        else:
            # Collect output after process has completed
            out, err = process.communicate()
            stdout_complete = escape_ansi(out.strip())

        return stdout_complete, err.strip(), process.returncode

    except subprocess.CalledProcessError as e:
        log("Error executing command")
        # Handle the exception for subprocess errors
        return e.output.strip(), e.stderr.strip(), e.returncode
    except Exception as e:
        log(f"Unexpected error: {str(e)}")
        return "", str(e), 255
