import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Morse Code Cipher - Encode and decode text to/from Morse code."
    )
    parser.add_argument(
        "operation",
        type=str,
        choices=["encode", "decode"],
        help="Operation to perform: 'encode' or 'decode'.",
    )
    parser.add_argument("text", type=str, help="The text to be encoded or decoded")
    return parser
