from trifid import TrifidCipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and execute encryption/decryption.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    cipher = TrifidCipher()

    if args.operation == "encrypt":
        try:
            encrypted_text = cipher.encrypt(args.text)
            print(f"Encrypted: {encrypted_text}")
        except ValueError as e:
            print(f"Error during encryption: {e}")
    elif args.operation == "decrypt":
        try:
            decrypted_text = cipher.decrypt(args.text)
            print(f"Decrypted: {decrypted_text}")
        except ValueError as e:
            print(f"Error during decryption: {e}")
    else:
        print("Please provide either --encrypt or --decrypt argument.")


if __name__ == "__main__":
    main()
