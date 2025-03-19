import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(description="Zobrist Hashing")
    parser.add_argument(
        "--board_size",
        type=int,
        required=True,
        help="Size of the board (number of squares)",
    )
    parser.add_argument(
        "--num_pieces",
        type=int,
        required=True,
        help="Number of different pieces (including empty squares)",
    )
    parser.add_argument(
        "--board_state",
        type=int,
        nargs="+",
        required=True,
        help="Current state of the board as a list of piece indices",
    )
    return parser
