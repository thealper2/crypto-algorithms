from xor8 import XOR8
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and execute the XOR8 operation.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    try:
        xor8 = XOR8(args.binary1, args.binary2)
        result = xor8.perform_xor()
        print(f"Result of XOR operation: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
