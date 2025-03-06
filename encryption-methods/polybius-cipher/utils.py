import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt text using the Polybius cipher."
    )
    parser.add_argument(
        "mode", choices=["encrypt", "decrypt"], help="Mode: 'encrypt' or 'decrypt'."
    )
    parser.add_argument("text", type=str, help="The text to encrypt or decrypt.")
    return parser
