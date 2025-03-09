from morse_code import MorseCodeCipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform Base92 encoding/decoding.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    cipher = MorseCodeCipher()

    try:
        if args.operation == "encode":
            # Encode the input string as bytes
            result = cipher.encode(args.text)
            print(f"Encoded: {result}")
        elif args.operation == "decode":
            # Decode the input string
            result = cipher.decode(args.text)
            print(f"Decoded: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
