from pearson import PearsonHashing
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and compute the Pearson hash.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    hasher = PearsonHashing()
    try:
        hash_value = hasher.hash(args.message)
        print(f"Pearson hash of '{args.message}': {hash_value}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
