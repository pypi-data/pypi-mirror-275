import ast
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken
from base64 import urlsafe_b64encode
from .exceptions import PasswordError, NoTargetFoundError

import logging

logger = logging.getLogger(__name__)
logger.level = logging.ERROR

DEFAULT_SALT = (
    b"\x89\x7f\xc8\x93\x1d\xb8\xd3\xea\x16\x91\x08\xad\x15\x96\x1b\xef"  # A fixed salt
)


def derive_key(password: str, salt: str = None) -> bytes:
    if not salt:
        salt = DEFAULT_SALT

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend(),
    )
    return urlsafe_b64encode(kdf.derive(password.encode()))


def encrypt_value(key: bytes, secure_value: str) -> str:
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(secure_value.value.encode()).decode()


def decrypt_value(key: bytes, encrypted_value: str) -> str:
    cipher_suite = Fernet(key)
    try:
        return cipher_suite.decrypt(encrypted_value.value.encode()).decode()
    except InvalidToken:
        raise PasswordError("The password is incorrect or the salt does not match.")


def process_file(
    file_path: str,
    key: bytes,
    encrypt: bool = True,
    dry_run: bool = False,
    verbose: bool = False,
):
    if verbose:
        logger.level = logging.INFO

    with open(file_path, "r+") as file:
        source = file.read()
        logger.info(f"Processing: {file_path}")
        tree = ast.parse(source, filename=file_path)
        modified_source = source
        found = False

    for node in ast.walk(tree):
        if isinstance(node, ast.AnnAssign) and isinstance(node.value, ast.Constant):
            if isinstance(node.annotation, ast.Name):
                if encrypt and node.annotation.id == "SecureString":
                    encrypted_value = encrypt_value(key, node.value)
                    modified_source = modified_source.replace(
                        node.value.value, encrypted_value
                    )
                    modified_source = modified_source.replace(
                        "SecureString", "EncryptedString"
                    )
                    found = True
                elif not encrypt and node.annotation.id == "EncryptedString":
                    decrypted_value = decrypt_value(key, node.value)
                    modified_source = modified_source.replace(
                        node.value.value, decrypted_value
                    )
                    modified_source = modified_source.replace(
                        "EncryptedString", "SecureString"
                    )
                    found = True

    if not found:
        if encrypt:
            raise NoTargetFoundError("No target SecureStrings found for encryption.")
        else:
            raise NoTargetFoundError("No target EncryptedStrings found for decryption.")

    if modified_source != source:
        if not dry_run:
            with open(file_path, "w") as file:
                file.write(modified_source)
                logger.info(f"Processed: {file_path}")
        else:
            logger.info(f"[DRY RUN] Processed file: {file_path}, did not save")
            return modified_source


def encrypt_file(file_path, password, salt=None, dryrun=False, verbose=False):
    if verbose:
        logger.level = logging.INFO

    key = derive_key(password, salt=salt)
    return process_file(file_path, key, encrypt=True, dry_run=dryrun, verbose=verbose)


def decrypt_file(file_path, password, salt=None, dryrun=False, verbose=False):
    if verbose:
        logger.level = logging.INFO

    key = derive_key(password, salt=salt)
    return process_file(file_path, key, encrypt=False, dry_run=dryrun, verbose=verbose)
