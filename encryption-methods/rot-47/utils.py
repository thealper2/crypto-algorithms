import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="ROT47 Cipher - Encrypt or decrypt text using ROT47."
    )
    parser.add_argument(
        "operation",
        type=str,
        choices=["encrypt", "decrypt"],
        help="Operation to perform: 'encrypt' or 'decrypt'",
    )
    parser.add_argument("text", type=str, help="The text to be encrypted or decrypted")
    return parser
