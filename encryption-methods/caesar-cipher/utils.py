import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt text using the Caesar cipher."
    )
    parser.add_argument(
        "operation", choices=["encrypt", "decrypt"], help="The operation to perform."
    )
    parser.add_argument("text", type=str, help="The text to encrypt or decrypt.")
    parser.add_argument(
        "--shift",
        type=int,
        default=3,
        help="The number of positions to shift the characters. Default is 3.",
    )
    parser.add_argument(
        "--brute-force",
        action="store_true",
        help="Use brute-force to decrpyt (only for decryption).",
    )
    return parser
