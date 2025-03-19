import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Compute the Pearson hash of a given message."
    )
    parser.add_argument("message", type=str, help="The message to hash.")
    return parser
