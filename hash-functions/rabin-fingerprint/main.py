from rabin import RabinFingerprint
from utils import setup_argparser


def main():
    """
    Main function to demonstrate the RabinFingerprint class using command-line arguments.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    # Initialize the RabinFingerprint class
    rabin = RabinFingerprint(base=args.base, modulus=args.modulus)

    # Compute the fingerprint
    fingerprint = rabin.compute(args.input)
    if fingerprint is not None:
        print(f"Rabin Fingerprint for '{args.input}': {fingerprint}")


if __name__ == "__main__":
    main()
