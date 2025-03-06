from bifid_cipher import BifidCipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform encryption/decryption.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    bifid = BifidCipher(key=args.key)
    if args.encrypt:
        result = bifid.encrypt(args.encrypt)
        print(f"Encrypted text: {result}")
    elif args.decrypt:
        result = bifid.decrypt(args.decrypt)
        print(f"Decrypted text: {result}")


if __name__ == "__main__":
    main()
