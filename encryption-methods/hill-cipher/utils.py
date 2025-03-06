import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Hill Cipher Encryption and Decryption"
    )
    parser.add_argument(
        "mode", choices=["encrypt", "decrypt"], help="Mode: 'encrypt' or 'decrypt'."
    )
    parser.add_argument("text", type=str, help="The text to encrypt or decrypt.")
    parser.add_argument(
        "--key",
        type=str,
        required=True,
        help="Key matrix as a comma-separated list (e.g., 6,24,1,13,16,10,20,17,15)",
    )
    return parser
