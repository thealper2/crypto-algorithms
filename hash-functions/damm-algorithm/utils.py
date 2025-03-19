import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(description="Damm Algorithm Implementation")
    parser.add_argument(
        "action",
        type=str,
        choices=["compute", "validate"],
        help="Action to perform: 'compute' to calculate check digit, 'validate' to validate a number.",
    )
    parser.add_argument("number", type=int, help="The number to compute or validate.")
    return parser
