from base_45 import Base45Cipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform Base45 encoding/decoding.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    base45 = Base45Cipher()

    try:
        if args.operation == "encode":
            # Encode the input string as bytes
            result = base45.encode(args.text.encode("utf-8"))
            print(f"Encoded: {result}")
        elif args.operation == "decode":
            # Decode the input string
            decoded_bytes = base45.decode(args.text)
            result = decoded_bytes.decode("utf-8")
            print(f"Decoded: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
