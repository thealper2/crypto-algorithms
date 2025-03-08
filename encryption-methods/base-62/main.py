from base_62 import Base62Cipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform Base62 encoding/decoding.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    base62 = Base62Cipher()

    try:
        if args.operation == "encode":
            # Encode the input string as bytes
            result = base62.encode(args.input)
            print(f"Encoded: {result}")
        elif args.operation == "decode":
            # Decode the input string
            result = base62.decode(args.input)
            print(f"Decoded: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
