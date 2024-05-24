class EncryptionError(Exception):
    """Base class for encryption-related errors."""

    pass


class DecryptionError(Exception):
    """Base class for decryption-related errors."""

    pass


class PasswordError(EncryptionError, DecryptionError):
    """Exception raised for errors involving the encryption or decryption key."""

    pass


class NoTargetFoundError(Exception):
    """Exception raised when no target strings are found for processing."""

    pass


class NoPasswordProvidedError(PasswordError):
    """Exception raised when no password is provided."""

    pass
