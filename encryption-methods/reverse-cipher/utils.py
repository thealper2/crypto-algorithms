import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Reverse Cipher Encryption and Decryption"
    )
    parser.add_argument(
        "operation",
        choices=["encrypt", "decrypt"],
        help="Operation to perform: encrypt or decrypt",
    )
    parser.add_argument("text", help="The text to encrypt or decrypt")
    return parser
