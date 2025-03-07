from lehmer_code import LehmerCode
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and execute Lehmer code operations.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    if args.encrypt:
        try:
            lehmer_code = LehmerCode.encrypt(args.encrypt)
            print(f"Lehmer Code: {lehmer_code}")
        except ValueError as e:
            print(f"Error: {e}")

    if args.decrypt:
        try:
            permutation = LehmerCode.decrypt(args.decrypt)
            print(f"Permutation: {permutation}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
