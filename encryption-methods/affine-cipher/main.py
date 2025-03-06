from affine_cipher import AffineCipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform encryption/decryption.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    cipher = AffineCipher(args.a, args.b)

    if args.operation == "encrypt":
        result = cipher.encrypt(args.text)
        print(f"Encrpyted: {result}")
    elif args.operation == "decrypt":
        result = cipher.decrypt(args.text, args.a, args.b)
        print(f"Decrypted: {result}")


if __name__ == "__main__":
    main()
