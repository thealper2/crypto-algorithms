import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(description="Chaocipher Encryption and Decryption")
    parser.add_argument(
        "--left", type=str, required=True, help="Left alphabet for the cipher."
    )
    parser.add_argument(
        "--right", type=str, required=True, help="Right alphabet for the cipher."
    )
    parser.add_argument("--encrypt", type=str, help="Text to encrypt.")
    parser.add_argument("--decrypt", type=str, help="Text to decrypt.")
    return parser
