import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Main function to handle command-line arguments and validate the number using the Luhn Algorithm.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Validate a number using the Luhn Algorithm."
    )
    parser.add_argument("number", type=str, help="The number to validate.")
    return parser
