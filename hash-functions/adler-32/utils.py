import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Compute the Adler-32 checksum of a given input."
    )
    parser.add_argument(
        "input", type=str, help="Input string to compute the Adler-32 checksum for."
    )
    return parser
