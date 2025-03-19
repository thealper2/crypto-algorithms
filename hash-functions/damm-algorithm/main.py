from damm import DammAlgorithm
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and execute the Damm Algorithm.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    damm = DammAlgorithm()

    try:
        if args.action == "compute":
            check_digit = damm.compute_check_digit(args.number)
            print(f"Check digit for {args.number} is: {check_digit}")
        elif args.action == "validate":
            is_valid = damm.validate_number(args.number)
            print(f"The number {args.number} is {'valid' if is_valid else 'invalid'}.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
