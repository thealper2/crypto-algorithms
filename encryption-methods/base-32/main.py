from base_32 import Base32Cipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform Base32 encoding/decoding.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    base32 = Base32Cipher()

    try:
        if args.operation == "encode":
            # Encode the input string as bytes
            result = base32.encode(args.text.encode("utf-8"))
            print(f"Encoded: {result}")
        elif args.operation == "decode":
            # Decode the input string
            decoded_bytes = base32.decode(args.text)
            result = decoded_bytes.decode("utf-8")
            print(f"Decoded: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
