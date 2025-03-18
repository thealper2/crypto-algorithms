from fletcher import Fletcher
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and compute/validate the Fletcher checksum.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    fletcher = Fletcher(args.data)

    if args.validate is not None:
        # Validate the checksum
        is_valid = Fletcher.validate_checksum(args.data, args.validate)
        print(f"Checksum validation result: {is_valid}")
    else:
        # Compute the checksum
        checksum = fletcher.compute_checksum()
        print(f"Computed Fletcher checksum: {checksum}")


if __name__ == "__main__":
    main()
