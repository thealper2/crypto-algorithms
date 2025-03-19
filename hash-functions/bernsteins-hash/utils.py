import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Compute Bernstein's Hash (DJB2) for a given string."
    )
    parser.add_argument("input_string", type=str, help="The string to hash.")
    return parser
