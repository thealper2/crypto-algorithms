import unittest
from crc import CRC


class TestCRC(unittest.TestCase):
    """
    A test class for the CRC implementation.
    """

    def test_crc_calculation_valid_data(self):
        """
        Test CRC calculation with valid hexadecimal data.
        """
        crc_calculator = CRC(
            polynomial=0x1021, initial_value=0xFFFF, final_xor_value=0x0000
        )
        data = [0x1A, 0x2B, 0x3C, 0x4D]  # Hexadecimal data as a list of bytes
        expected_crc = 0x29B1  # Expected CRC value for the given data
        self.assertEqual(crc_calculator.calculate_crc(data), expected_crc)

    def test_crc_calculation_empty_data(self):
        """
        Test CRC calculation with empty data.
        """
        crc_calculator = CRC(
            polynomial=0x1021, initial_value=0xFFFF, final_xor_value=0x0000
        )
        data = []  # Empty data
        expected_crc = 0xFFFF ^ 0x0000  # Initial value XOR final XOR value
        self.assertEqual(crc_calculator.calculate_crc(data), expected_crc)

    def test_hex_string_to_bytes_valid_input(self):
        """
        Test conversion of a valid hex string to a list of bytes.
        """
        crc_calculator = CRC(polynomial=0x1021)
        hex_str = "1A2B3C4D"
        expected_bytes = [0x1A, 0x2B, 0x3C, 0x4D]
        self.assertEqual(crc_calculator.hex_string_to_bytes(hex_str), expected_bytes)

    def test_hex_string_to_bytes_invalid_input(self):
        """
        Test conversion of an invalid hex string (odd number of characters).
        """
        crc_calculator = CRC(polynomial=0x1021)
        hex_str = "1A2B3C4"  # Invalid hex string (odd number of characters)
        with self.assertRaises(ValueError):
            crc_calculator.hex_string_to_bytes(hex_str)

    def test_hex_string_to_bytes_non_hex_input(self):
        """
        Test conversion of a non-hexadecimal string.
        """
        crc_calculator = CRC(polynomial=0x1021)
        hex_str = "1G2B3C4D"  # Invalid hex string (contains 'G')
        with self.assertRaises(ValueError):
            crc_calculator.hex_string_to_bytes(hex_str)

    def test_crc_calculation_with_different_polynomial(self):
        """
        Test CRC calculation with a different polynomial.
        """
        crc_calculator = CRC(
            polynomial=0x8005, initial_value=0x0000, final_xor_value=0x0000
        )
        data = [0x01, 0x02, 0x03, 0x04]
        expected_crc = 0x4C3A  # Expected CRC value for the given data and polynomial
        self.assertEqual(crc_calculator.calculate_crc(data), expected_crc)

    def test_crc_calculation_with_final_xor(self):
        """
        Test CRC calculation with a non-zero final XOR value.
        """
        crc_calculator = CRC(
            polynomial=0x1021, initial_value=0xFFFF, final_xor_value=0xFFFF
        )
        data = [0x1A, 0x2B, 0x3C, 0x4D]
        expected_crc = 0x29B1 ^ 0xFFFF  # Expected CRC value XOR final XOR value
        self.assertEqual(crc_calculator.calculate_crc(data), expected_crc)


if __name__ == "__main__":
    unittest.main()
