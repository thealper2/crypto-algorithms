from adler32 import Adler32
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and compute the Adler-32 checksum.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    # Convert input string to bytes
    data = args.input.encode("utf-8")

    # Compute Adler-32 checksum
    adler32 = Adler32()
    adler32.update(data)
    checksum = adler32.hexdigest()

    print(f"Adler-32 checksum: {checksum}")


if __name__ == "__main__":
    main()
