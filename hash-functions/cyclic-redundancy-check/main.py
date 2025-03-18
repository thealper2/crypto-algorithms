from crc import CRC
from utils import setup_argparser


def main():
    """
    Main function to parse command-line arguments and calculate CRC.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    try:
        polynomial = int(args.polynomial, 16)
        initial_value = int(args.initial_value, 16)
        final_xor_value = int(args.final_xor_value, 16)

        crc_calculator = CRC(polynomial, initial_value, final_xor_value)
        data_bytes = crc_calculator.hex_string_to_bytes(args.data)
        crc_value = crc_calculator.calculate_crc(data_bytes)

        print(f"CRC Value: 0x{crc_value:04X}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
