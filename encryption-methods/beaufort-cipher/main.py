from beaufort_cipher import BeaufortCipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform encryption/decryption.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    try:
        cipher = BeaufortCipher(args.key)

        if args.encrypt:
            encrypted_text = cipher.encrypt(args.encrypt)
            print(f"Encrypted: {encrypted_text}")
        elif args.decrypt:
            decrypted_text = cipher.decrypt(args.decrypt)
            print(f"Decrypted: {decrypted_text}")
        else:
            print("Please provide either --encrypt or --decrypt argument.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
