from tabulation_hashing import TabulationHashing
from utils import setup_argparser


def main():
    """
    Main function to demonstrate the usage of TabulationHashing.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    try:
        hasher = TabulationHashing(table_size=args.table_size, key_size=args.key_size)
        hash_value = hasher.hash(args.key)
        print(f"Hash value for key {args.key}: {hash_value}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
