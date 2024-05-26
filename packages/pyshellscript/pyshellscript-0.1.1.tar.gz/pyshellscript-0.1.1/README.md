# PyShellScript

This project provides a Python-based wrapper for executing and managing local and remote commands without the need for
Bash scripting. It leverages `paramiko` for SSH communication and `subprocess` for local command execution, and includes
live log streaming capabilities.

## Features

- **Remote Command Execution**: Utilize `paramiko` to execute commands on remote servers via SSH.
- **Local Command Execution**: Use `subprocess` to run commands locally on your system.
- **Live Log Streaming**: Stream command outputs in real-time, facilitating live monitoring of command execution for
  both Remote and Local command Executions
- **Python-Centric**: Manage all functionalities directly from Python scripts, enhancing script automation and
  integration.

## Getting Started

### Installation

Install by pip:

```bash
pip install pyshellscript
``` 

clone this repository:

```bash
git clone https://github.com/dk-tgz/PyShellScript
```

### Examples in https://github.com/dk-tgz/PyShellScript/tree/main/examples

