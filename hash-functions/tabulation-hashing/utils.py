import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(description="Tabulation Hashing Implementation")
    parser.add_argument("--key", type=int, required=True, help="The key to hash.")
    parser.add_argument(
        "--table_size", type=int, default=256, help="The size of the hash table."
    )
    parser.add_argument(
        "--key_size", type=int, default=8, help="The size of the key in bytes."
    )
    return parser
