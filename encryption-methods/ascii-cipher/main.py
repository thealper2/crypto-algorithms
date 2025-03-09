from ascii_cipher import ASCIICipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and execute encoding/decoding.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    try:
        cipher = ASCIICipher(args.shift)

        if args.operation == "encrypt":
            result = cipher.encrypt(args.text)
            print(f"Encoded message: {result}")
        elif args.operation == "decrypt":
            result = cipher.decrypt(args.text)
            print(f"Decoded message: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
