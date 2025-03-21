from sha256 import SHA256
from utils import setup_argparser


def main():
    """Main function to handle command-line arguments and compute SHA-256 hash."""
    parser = setup_argparser()
    args = parser.parse_args()

    sha256 = SHA256()
    try:
        hash_value = sha256.hash(args.message.encode("utf-8"))
        print(f"SHA-256 hash: {hash_value}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
