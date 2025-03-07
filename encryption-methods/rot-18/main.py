from rot18 import ROT18Cipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform ROT18 encryption/decryption.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    rot18 = ROT18Cipher()

    if args.operation == "encrypt":
        result = rot18.encrypt(args.text)
        print(f"Encrypted text: {result}")
    elif args.operation == "decrypt":
        result = rot18.decrypt(args.text)
        print(f"Decrypted text: {result}")


if __name__ == "__main__":
    main()
