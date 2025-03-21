import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt text using the Scytale cipher."
    )
    parser.add_argument(
        "--key", type=int, required=True, help="Number of rows for the Scytale cipher.."
    )
    parser.add_argument("--encrypt", type=str, help="The plaintext to encrypt.")
    parser.add_argument("--decrypt", type=str, help="The ciphertext to decrypt.")
    return parser
