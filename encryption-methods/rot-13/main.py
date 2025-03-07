from rot13 import ROT13Cipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform ROT13 encryption/decryption.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    cipher = ROT13Cipher()
    result = cipher.encrypt_decrypt(args.text)

    if result is not None:
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
