from verhoeff import VerhoeffAlgorithm
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and execute the Verhoeff Algorithm.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    verhoeff = VerhoeffAlgorithm()
    try:
        if args.validate:
            is_valid = verhoeff.validate_number(args.number)
            print(f"The number {args.number} is {'valid' if is_valid else 'invalid'}.")
        else:
            checksum = verhoeff.compute_checksum(args.number)
            print(f"The checksum digit for {args.number} is {checksum}.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
