from base_92 import Base92Cipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform Base92 encoding/decoding.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    base92 = Base92Cipher()

    try:
        if args.operation == "encode":
            # Encode the input string as bytes
            result = base92.encode(args.text.encode("utf-8"))
            print(f"Encoded: {result}")
        elif args.operation == "decode":
            # Decode the input string
            result = base92.decode(args.text).encode("utf-8")
            print(f"Decoded: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
