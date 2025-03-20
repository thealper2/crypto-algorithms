import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Generate HMAC using a custom hash function."
    )
    parser.add_argument("--key", type=str, required=True, help="Secret key for HMAC.")
    parser.add_argument(
        "--message", type=str, required=True, help="Message to authenticate."
    )
    return parser


def custom_hash_function(data: bytes) -> bytes:
    """
    A simple custom hash function for demonstration purposes.
    This is a placeholder and should be replaced with a secure hash function.

    Args:
        data (bytes): Input data to hash.

    Returns:
        bytes: Hashed data as bytes.
    """
    # This is a dummy hash function (not secure)
    return bytes([byte ^ 0xFF for byte in data])
