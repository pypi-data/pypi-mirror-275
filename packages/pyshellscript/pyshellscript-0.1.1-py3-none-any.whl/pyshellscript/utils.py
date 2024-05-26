import json
import re
from loguru import logger
from paramiko import RSAKey


def read_output(stream):
    """
    Read all lines from a stream and decode them from UTF-8.

    Args:
        stream (IO): The stream to read from.

    Returns:
        list: A list of decoded lines.
    """
    output = [line.decode("utf-8") for line in iter(stream.readline, b"")]
    stream.close()
    return output


def log(*args, sep=" "):
    """
    Log a message with the specified arguments using Loguru.

    Args:
        *args: Arguments to log.
        sep (str): Separator to use between arguments.
    """
    message = sep.join(map(str, args))
    logger.opt(depth=1).info(message)


def escape_ansi(line):
    """
    Remove ANSI escape sequences from a line of text.

    Args:
        line (str): The input text with potential ANSI codes.

    Returns:
        str: The text stripped of ANSI escape codes.
    """
    ansi_escape = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]")
    return ansi_escape.sub("", line)


def get_value_from_json(file_path, key):
    """
    Load a JSON file and return the value for a specified key.

    Args:
        file_path (str): The path to the JSON file.
        key (str): The key to retrieve the value for.

    Returns:
        Any: The value associated with 'key' in the JSON file, or None if not found.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data.get(key)
    except (FileNotFoundError, json.JSONDecodeError) as error:
        logger.error(f"Failed to load or parse JSON file {file_path}: {error}")
        return None


def generate_keys(public_key_path="./id_rsa_env.pub", private_key_path="./id_rsa_key.pem"):
    """
    Generates and saves RSA public and private keys.

    Returns:
        tuple: Paths to the generated public and private key files.
    """
    key = RSAKey.generate(2048)
    try:
        with open(private_key_path, 'w') as private_file:
            key.write_private_key(private_file)
        with open(public_key_path, 'w') as public_file:
            public_file.write(f"{key.get_name()} {key.get_base64()} generated-by-paramiko\n")
    except IOError as e:
        logger.error(f"Error writing keys to files: {e}")
    return public_key_path, private_key_path
