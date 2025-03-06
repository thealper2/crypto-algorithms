import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt text using the Bifid cipher."
    )
    parser.add_argument(
        "--key", type=str, required=True, help="The key to use for the Polybius square."
    )
    parser.add_argument("--encrypt", type=str, help="The plaintext to encrypt.")
    parser.add_argument("--decrypt", type=str, help="The ciphertext to decrypt.")
    return parser
