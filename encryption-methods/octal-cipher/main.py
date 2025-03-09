from octal_cipher import OctalCipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and execute encoding/decoding.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    try:
        cipher = OctalCipher()

        if args.operation == "encode":
            result = cipher.encode(args.text)
            print(f"Encoded message: {result}")
        elif args.operation == "decode":
            result = cipher.decode(args.text)
            print(f"Decoded message: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
