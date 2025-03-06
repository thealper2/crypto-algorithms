from polybius_cipher import PolybiusCipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform encryption or decryption.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    polybius = PolybiusCipher()

    try:
        if args.mode == "encrypt":
            result = polybius.encrypt(args.text)
            print(f"Encrypted text: {result}")
        elif args.mode == "decrypt":
            result = polybius.decrypt(args.text)
            print(f"Decrypted text: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
