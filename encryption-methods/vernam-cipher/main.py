from vernam_cipher import VernamCipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform encryption/decryption.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    vernam = VernamCipher()

    try:
        if args.operation == "encrypt":
            result = vernam.encrypt(args.text, args.key)
            print(f"Encrypted Ciphertext: {result}")
        elif args.operation == "decrypt":
            result = vernam.decrypt(args.text, args.key)
            print(f"Decrypted Plaintext: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
