from zobrist import ZobristHashing
from utils import setup_argparser


def main():
    """
    Main function to demonstrate the usage of ZobristHashing class.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    try:
        zobrist = ZobristHashing(args.board_size, args.num_pieces)
        hash_value = zobrist.compute_hash(args.board_state)
        print(f"Computed Zobrist Hash: {hash_value}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
