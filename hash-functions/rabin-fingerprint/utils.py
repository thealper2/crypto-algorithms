import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Compute the Rabin Fingerprint of a string."
    )
    parser.add_argument(
        "input", type=str, help="The input string to compute the fingerprint for."
    )
    parser.add_argument(
        "--base",
        type=int,
        default=256,
        help="The base value for the polynomial rolling hash.",
    )
    parser.add_argument(
        "--modulus",
        type=int,
        default=101,
        help="The modulus value for the polynomial rolling hash.",
    )
    return parser
