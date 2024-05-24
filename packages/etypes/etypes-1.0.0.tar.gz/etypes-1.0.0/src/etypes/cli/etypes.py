import os
import logging
import click

from etypes.processor import derive_key, encrypt_file, decrypt_file

logger = logging.getLogger(__name__)
logger.level = logging.ERROR


@click.group()
def main():
    pass


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
    )
)
@click.argument("file_path")
@click.option("-p", "--password", help="password for specified file_path")
@click.option("-pf", "--password-file", help="password file for specified file_path")
@click.option("-s", "--salt", help="optional salt for specified file_path")
@click.option("--dryrun", is_flag=True, default=False, help="Dry run verbose mode")
@click.option(
    "-v", "--verbose", is_flag=True, default=False, help="Enables verbose mode"
)
def encrypt(file_path, password, password_file, salt, dryrun, verbose):

    if verbose:
        logger.level = logging.INFO

    if password_file:
        if not os.path.isfile(password_file):
            raise FileNotFoundError(password_file)
        with open(password_file, "r") as file:
            password = file.read().strip()
        logger.info(f"Loaded password file {password_file}")

    if not os.path.isfile(file_path):
        raise FileNotFoundError(file_path)

    encrypt_file(file_path, password, salt=salt, dryrun=dryrun, verbose=verbose)
    logger.info(f"Encrypted file {password_file}")


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
    )
)
@click.argument("file_path")
@click.option("-p", "--password", help="password for specified file_path")
@click.option("-pf", "--password-file", help="password file for specified file_path")
@click.option("-s", "--salt", help="optional salt for specified file_path")
@click.option("--dryrun", is_flag=True, default=False, help="Dry run verbose mode")
@click.option(
    "-v", "--verbose", is_flag=True, default=False, help="Enables verbose mode"
)
def decrypt(file_path, password, password_file, salt, dryrun, verbose):

    if verbose:
        logger.level = logging.INFO

    if password_file:
        if not os.path.isfile(password_file):
            raise FileNotFoundError(password_file)
        with open(password_file, "r") as file:
            password = file.read().strip()
        logger.info(f"Loaded password file {password_file}")

    if not os.path.isfile(file_path):
        raise FileNotFoundError(file_path)

    decrypt_file(file_path, password, salt=salt, dryrun=dryrun, verbose=verbose)
    logger.info(f"Decrypted file {password_file}")


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
    )
)
@click.argument("file")
def dump():
    pass


@click.command(
    context_settings=dict(
        ignore_unknown_options=True,
    )
)
@click.argument("config")
def verify():
    pass


main.add_command(encrypt)
main.add_command(decrypt)
main.add_command(verify)
main.add_command(dump)
