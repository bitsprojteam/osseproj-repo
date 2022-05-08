import uuid
import datetime
import argparse
import os

def str_uuid():
    """
    Returns a uuid4 as a string
    """
    return str(uuid.uuid4())

# Function to convert string to datetime
def converter(dt):
    format = '%b %d %Y %I:%M%p'  # You have to specify the format either statically or dynamically
    datetime_str = datetime.datetime.strptime(dt, format)
    return datetime_str


def str2unix(input_str: str) -> str:
    r"""
    Converts the string from \r\n line endings to \n

    Parameters
    ----------
    input_str
        The string whose line endings will be converted

    Returns
    -------
        The converted string
    """
    r_str = input_str.replace('\r\n', '\n')
    return r_str


def dos2unix(source_file: str, dest_file: str):
    """
    Converts a file that contains Dos like line endings into Unix like

    Parameters
    ----------
    source_file
        The path to the source file to be converted
    dest_file
        The path to the converted file for output
    """
    # NOTE: Could add file existence checking and file overwriting
    # protection
    with open(source_file, 'r') as reader:
        dos_content = reader.read()

    unix_content = str2unix(dos_content)

    with open(dest_file, 'w') as writer:
        writer.write(unix_content)
