import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Lehmer Code Encryption and Decryption"
    )
    parser.add_argument(
        "--encrypt", type=int, nargs="+", help="Permutation to encrypt (e.g., 3 1 2)"
    )
    parser.add_argument(
        "--decrypt", type=int, nargs="+", help="Lehmer code to decrypt (e.g., 2 0 0)"
    )
    return parser
