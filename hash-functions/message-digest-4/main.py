from md4 import MD4
from utils import setup_argparser


def main():
    """Main function to handle command-line arguments and compute MD4 hash."""
    parser = setup_argparser()
    args = parser.parse_args()

    try:
        md4 = MD4()
        message = args.message.encode("utf-8")
        hash_result = md4.hash(message)
        print(f"MD4 Hash: {hash_result.hex()}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
