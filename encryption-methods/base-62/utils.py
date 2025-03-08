import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(description="Base62 Encoder and Decoder")
    parser.add_argument(
        "operation",
        type=str,
        choices=["encode", "decode"],
        help="Operation to perform: 'encode' or 'decode'",
    )
    parser.add_argument("input", type=int, help="The input to be encoded or decoded")
    return parser
