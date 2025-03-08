from base_85 import Base85Cipher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform Base85 encoding/decoding.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    base85 = Base85Cipher()

    try:
        if args.operation == "encode":
            data = args.text.encode("utf-8")
            result = base85.encode(data)
            print("Encoded:", result)

        elif args.operation == "decode":
            encoded = args.text
            result = base85.decode(encoded)
            print("Decoded:", result)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
