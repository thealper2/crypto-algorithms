import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Compute the MD5 hash of a given input message."
    )
    parser.add_argument("message", type=str, help="The input message to hash.")
    return parser
