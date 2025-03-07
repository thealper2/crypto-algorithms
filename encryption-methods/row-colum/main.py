from row_column import RowColumnCipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform encryption or decryption.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    cipher = RowColumnCipher(args.text, args.cols)

    if args.operation == "encrypt":
        result = cipher.encrypt()
        print(f"Encrypted Text: {result}")
    elif args.operation == "decrypt":
        result = cipher.decrypt(args.text)
        print(f"Decrypted Text: {result}")


if __name__ == "__main__":
    main()
