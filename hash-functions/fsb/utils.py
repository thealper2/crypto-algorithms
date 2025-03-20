import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Fast Syndrome-based Hash Function (FSB) Implementation"
    )
    parser.add_argument(
        "--n", type=int, required=True, help="Length of the binary code"
    )
    parser.add_argument(
        "--k",
        type=int,
        required=True,
        help="Length of the message (number of parity rows)",
    )
    parser.add_argument(
        "--t",
        type=int,
        required=True,
        help="Number of ones per row in the parity-check matrix",
    )
    parser.add_argument(
        "--message", type=str, required=True, help="Binary message (e.g., 101010...)"
    )
    return parser
