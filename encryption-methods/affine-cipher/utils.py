import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Affine Cipher Encryption and Decryption"
    )
    parser.add_argument(
        "operation",
        choices=["encrypt", "decrypt"],
        help="Operation to perform: encrypt or decrypt",
    )
    parser.add_argument("text", help="The text to encrypt or decrypt")
    parser.add_argument(
        "--a", type=int, default=5, help="The multiplicative key (default: 5)"
    )
    parser.add_argument(
        "--b", type=int, default=8, help="The additive key (default: 8)"
    )
    return parser
