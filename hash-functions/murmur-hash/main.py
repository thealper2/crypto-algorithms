from murmur import MurmurHash
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and compute the MurmurHash.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    murmur = MurmurHash(seed=args.seed)
    try:
        hash_value = murmur.hash(args.input)
        print(f"MurmurHash3 of '{args.input}' with seed {args.seed}: {hash_value}")
    except TypeError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
