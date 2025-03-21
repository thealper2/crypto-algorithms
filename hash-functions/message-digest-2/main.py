from md2 import MD2
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and compute the MD2 hash.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    md2 = MD2()
    try:
        hash_value = md2.hash(args.message.encode("utf-8"))
        print(f"MD2 Hash: {hash_value}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
