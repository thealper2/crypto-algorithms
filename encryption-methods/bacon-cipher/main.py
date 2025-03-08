from bacon_cipher import BaconCipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and execute encoding/decoding.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    bacon_cipher = BaconCipher()

    try:
        if args.operation == "encrypt":
            result = bacon_cipher.encode(args.text)
            print(f"Encoded message: {result}")
        elif args.operation == "decrypt":
            result = bacon_cipher.decode(args.text)
            print(f"Decoded message: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
