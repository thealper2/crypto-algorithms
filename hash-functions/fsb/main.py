from fsb import FSBHash
from utils import setup_argparser


def main() -> None:
    """
    Main function to run FSB hashing.
    """
    try:
        parser = setup_argparser()
        args = parser.parse_args()
        fsb = FSBHash(n=args.n, k=args.k, t=args.t)
        print("Parity-check matrix (H):")
        fsb.print_matrix()

        try:
            message = [int(bit) for bit in args.message]
            if len(message) != args.n:
                raise ValueError(
                    f"Message length ({len(message)}) does not match n ({args.n})"
                )
            if any(bit not in (0, 1) for bit in message):
                raise ValueError("Message must contain only 0s and 1s")
        except ValueError as e:
            raise ValueError(f"Invalid message input: {e}")

        hash_output = fsb.hash(message)
        print(f"Input Message: {''.join(str(b) for b in message)}")
        print(f"Syndrome (Hash Output): {''.join(str(b) for b in hash_output)}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
