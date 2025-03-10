from luhn_algorithm import LuhnAlgorithm
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and validate the number using the Luhn Algorithm.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    try:
        luhn = LuhnAlgorithm(args.number)
        if luhn.is_valid():
            print(
                f"The number '{args.number}' is valid according to the Luhn Algorithm."
            )
        else:
            print(
                f"The number '{args.number}' is NOT valid according to the Luhn Algorithm."
            )
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
