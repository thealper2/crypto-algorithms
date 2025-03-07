import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(description="ROT5 Cipher Implementation")
    parser.add_argument(
        "action",
        choices=["encrypt", "decrypt"],
        help="Action to perform: 'encrypt' or 'decrypt'.",
    )
    parser.add_argument("text", type=str, help="The text to encrypt or decrypt.")
    return parser
