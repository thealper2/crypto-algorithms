from caesar_cipher import CaesarCipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform encryption/decryption.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    cipher = CaesarCipher(shift=args.shift)

    if args.operation == "encrypt":
        result = cipher.encrypt(args.text)
        print(f"Encrypted text: {result}")
    elif args.operation == "decrypt":
        if args.brute_force:
            result = cipher.decrypt(args.text)
        else:
            result = cipher.decrypt(args.text, args.shift)
            print(f"Decrypted text: {result}")


if __name__ == "__main__":
    main()
