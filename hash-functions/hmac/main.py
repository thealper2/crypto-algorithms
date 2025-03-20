from hmac import HMAC
from utils import setup_argparser, custom_hash_function


def main():
    """
    Main function to handle command-line arguments and generate HMAC.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    try:
        # Convert key and message to bytes
        key = args.key.encode("utf-8")
        message = args.message.encode("utf-8")

        # Create HMAC instance
        hmac_generator = HMAC(key, message, custom_hash_function)

        # Generate and print HMAC
        hmac = hmac_generator.generate()
        print(f"Generated HMAC: {hmac.hex()}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
