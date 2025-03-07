import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(
        description="Rail Fence Cipher Encryption and Decryption"
    )
    parser.add_argument(
        "operation",
        type=str,
        choices=["encrypt", "decrypt"],
        help="Operation to perform: 'encrypt' or 'decrypt'",
    )
    parser.add_argument("text", type=str, help="The text to be encrypted or decrypted")
    parser.add_argument(
        "--rails", type=int, required=True, help="Number of rails to use for the cipher"
    )
    return parser
