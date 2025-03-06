from vigenere_cipher import VigenereCipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform encryption/decryption.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    try:
        cipher = VigenereCipher(args.key)
        if args.encrypt:
            encrypted_text = cipher.encrypt(args.encrypt)
            print(f"Encrypted Text: {encrypted_text}")
        elif args.decrypt:
            decrypted_text = cipher.decrypt(args.decrypt)
            print(f"Decrypted Text: {decrypted_text}")
        else:
            print("Please provide either --encrypt or --decrypt argument.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
