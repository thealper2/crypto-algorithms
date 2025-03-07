from rail_fence import RailFenceCipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform encryption or decryption.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    try:
        cipher = RailFenceCipher(args.rails)
        if args.operation == "encrypt":
            result = cipher.encrypt(args.text)
            print(f"Encrypted text: {result}")
        else:
            result = cipher.decrypt(args.text)
            print(f"Decrypted text: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
