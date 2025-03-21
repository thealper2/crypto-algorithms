from md5 import MD5
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and compute the MD5 hash.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    md5 = MD5()
    try:
        hash_value = md5.compute_md5(args.message)
        print(f"MD5 Hash: {hash_value}")
    except RuntimeError as e:
        print(e)


if __name__ == "__main__":
    main()
