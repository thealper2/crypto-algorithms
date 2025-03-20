import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Compute the MurmurHash3 of a given input."
    )
    parser.add_argument("input", type=str, help="The input string to hash.")
    parser.add_argument(
        "--seed",
        type=int,
        default=0,
        help="Seed value for the hash function. Default is 0.",
    )
    return parser
