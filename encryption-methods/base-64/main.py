from base_64 import Base64Cipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform encoding/decoding.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    cipher = Base64Cipher()

    try:
        if args.operation == "encode":
            result = cipher.encode(args.text)
            print(f"Encoded: {result}")
        elif args.operation == "decode":
            result = cipher.decode(args.text)
            print(f"Decoded: {result.decode('utf-8')}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
