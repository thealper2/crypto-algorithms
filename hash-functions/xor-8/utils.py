import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Perform an 8-bit XOR operation on two binary strings."
    )
    parser.add_argument("binary1", type=str, help="The first 8-bit binary string.")
    parser.add_argument("binary2", type=str, help="The second 8-bit binary string.")
    return parser
