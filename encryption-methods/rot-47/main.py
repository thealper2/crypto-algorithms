from rot47 import ROT47Cipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and execute the ROT47 cipher.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    cipher = ROT47Cipher()

    try:
        if args.operation == "encrypt":
            result = cipher.encrypt(args.text)
        else:
            result = cipher.decrypt(args.text)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
