import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Main function to parse command-line arguments and calculate CRC.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(description="Calculate CRC for given data.")
    parser.add_argument(
        "data", type=str, help="Data in hexadecimal format to calculate CRC for."
    )
    parser.add_argument(
        "--polynomial",
        type=str,
        default="0x1021",
        help="Polynomial for CRC calculation in hexadecimal format. Default is 0x1021.",
    )
    parser.add_argument(
        "--initial_value",
        type=str,
        default="0xFFFF",
        help="Initial value for CRC calculation in hexadecimal format. Default is 0xFFFF.",
    )
    parser.add_argument(
        "--final_xor_value",
        type=str,
        default="0x0000",
        help="Final XOR value for CRC calculation in hexadecimal format. Default is 0x0000.",
    )
    return parser
