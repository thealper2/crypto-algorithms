import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Compute or validate the Fletcher checksum for a given string."
    )
    parser.add_argument("data", type=str, help="The input string for the checksum.")
    parser.add_argument(
        "--validate", type=int, help="Validate the checksum against the provided value."
    )
    return parser
