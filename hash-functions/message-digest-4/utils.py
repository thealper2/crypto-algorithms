import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(description="Compute the MD4 hash of a message.")
    parser.add_argument("message", type=str, help="The message to hash.")
    return parser
