import unittest
from xor8 import XOR8


class TestXOR8(unittest.TestCase):
    """
    A test class for the XOR8 implementation.
    """

    def test_valid_input(self):
        """
        Test the XOR operation with valid 8-bit binary inputs.
        """
        xor8 = XOR8("10101010", "11001100")
        result = xor8.perform_xor()
        self.assertEqual(result, "01100110", "XOR operation failed for valid inputs.")

    def test_invalid_input_length(self):
        """
        Test the XOR operation with invalid input lengths (not 8 bits).
        """
        with self.assertRaises(ValueError):
            XOR8("1010101", "11001100")  # First input is 7 bits
        with self.assertRaises(ValueError):
            XOR8("10101010", "110011001")  # Second input is 9 bits

    def test_invalid_input_characters(self):
        """
        Test the XOR operation with inputs containing non-binary characters.
        """
        with self.assertRaises(ValueError):
            XOR8("1010101a", "11001100")  # First input contains 'a'
        with self.assertRaises(ValueError):
            XOR8("10101010", "1100110b")  # Second input contains 'b'

    def test_edge_case_all_zeros(self):
        """
        Test the XOR operation when both inputs are all zeros.
        """
        xor8 = XOR8("00000000", "00000000")
        result = xor8.perform_xor()
        self.assertEqual(result, "00000000", "XOR operation failed for all zeros.")

    def test_edge_case_all_ones(self):
        """
        Test the XOR operation when both inputs are all ones.
        """
        xor8 = XOR8("11111111", "11111111")
        result = xor8.perform_xor()
        self.assertEqual(result, "00000000", "XOR operation failed for all ones.")

    def test_edge_case_mixed_bits(self):
        """
        Test the XOR operation with mixed bits (e.g., alternating 0s and 1s).
        """
        xor8 = XOR8("01010101", "10101010")
        result = xor8.perform_xor()
        self.assertEqual(result, "11111111", "XOR operation failed for mixed bits.")

    def test_edge_case_one_input_all_zeros(self):
        """
        Test the XOR operation when one input is all zeros and the other is not.
        """
        xor8 = XOR8("00000000", "11111111")
        result = xor8.perform_xor()
        self.assertEqual(
            result, "11111111", "XOR operation failed when one input is all zeros."
        )

    def test_edge_case_one_input_all_ones(self):
        """
        Test the XOR operation when one input is all ones and the other is not.
        """
        xor8 = XOR8("11111111", "01010101")
        result = xor8.perform_xor()
        self.assertEqual(
            result, "10101010", "XOR operation failed when one input is all ones."
        )


if __name__ == "__main__":
    unittest.main()
