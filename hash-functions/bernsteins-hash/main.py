from djb2 import DJB2Hash
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and compute the DJB2 hash.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    try:
        # Create an instance of the DJB2Hash class
        djb2 = DJB2Hash()
        # Update the hash with the input string
        djb2.update(args.input_string)
        # Output the hash in integer and hexadecimal formats
        print(f"Hash (int): {djb2.digest()}")
        print(f"Hash (hex): {djb2.hexdigest()}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
