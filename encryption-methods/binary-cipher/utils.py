import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(description="Binary Cipher Encoder and Decoder")
    parser.add_argument(
        "operation",
        choices=["encode", "decode"],
        help="Operation to perform: encode or decode",
    )
    parser.add_argument("text", help="The text to encode or decode")
    return parser
