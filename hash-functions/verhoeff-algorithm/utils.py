import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Verhoeff Algorithm for checksum validation."
    )
    parser.add_argument(
        "number", type=str, help="The number to compute or validate the checksum."
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate the number instead of computing the checksum.",
    )
    return parser
