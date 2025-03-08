from atbash import AtbashCipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform encryption/decryption.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    cipher = AtbashCipher()

    if args.operation == "encrypt":
        try:
            encrypted_text = cipher.encrypt(args.text)
            print(f"Encrypted: {encrypted_text}")
        except ValueError as e:
            print(f"Error: {e}")

    if args.operation == "decrypt":
        try:
            decrypted_text = cipher.decrypt(args.text)
            print(f"Decrypted: {decrypted_text}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
