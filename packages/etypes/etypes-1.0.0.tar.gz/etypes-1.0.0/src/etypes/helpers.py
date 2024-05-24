import os
from .exceptions import NoPasswordProvidedError
from .processor import decrypt_file
from .utils import create_temporary_copy


def dynamic_import(globals, file_path, password=None, password_file=None, salt=None):

    if not password and not password_file:
        raise NoPasswordProvidedError(f"No password or password_file was provided")

    if password_file:
        if not os.path.isfile(password_file):
            raise FileNotFoundError(f"Could not find password_file {password_file}")
        with open(password_file, "r") as file:
            password = file.read()

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Could not find {file_path}")

    modified_source = None
    with create_temporary_copy(file_path) as fp:
        temp_file_path = fp.name
        decrypt_file(temp_file_path, password=password)
        modified_source = open(temp_file_path, "r").read()

    exec(modified_source, globals)
    return globals
