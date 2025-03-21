import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(description="ROT13 Encryption/Decryption Tool")
    parser.add_argument("text", type=str, help="The text to be encrypted or decrypted")
    return parser
