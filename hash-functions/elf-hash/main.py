from elf import ElfHash
from utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and compute the Elf Hash.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    elf_hash = ElfHash()
    try:
        hash_value = elf_hash.compute_hash(args.input_string)
        print(f"Elf Hash for '{args.input_string}': {hash_value}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
