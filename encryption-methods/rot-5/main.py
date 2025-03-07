from rot5 import ROT5Cipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and execute the ROT5 cipher.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    rot5 = ROT5Cipher()

    try:
        if args.action == "encrypt":
            result = rot5.encrypt(args.text)
        else:
            result = rot5.decrypt(args.text)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
