import unittest
from base_32 import Base32Cipher


class TestBase32Cipher(unittest.TestCase):
    """
    Test suite for the Base32Cipher class.
    """

    def setUp(self):
        """
        Set up the Base32Cipher instance for testing.
        """
        self.base32 = Base32Cipher()

    def test_encode_empty_input(self):
        """
        Test encoding with empty input. Expect a ValueError to be raised.
        """
        with self.assertRaises(ValueError):
            self.base32.encode(b"")

    def test_decode_empty_input(self):
        """
        Test decoding with empty input. Expect a ValueError to be raised.
        """
        with self.assertRaises(ValueError):
            self.base32.decode("")

    def test_encode_basic(self):
        """
        Test encoding with basic input.
        """
        input_data = b"Hello"
        expected_output = "JBSWY3DP"
        self.assertEqual(self.base32.encode(input_data), expected_output)

    def test_decode_basic(self):
        """
        Test decoding with basic input.
        """
        input_data = "JBSWY3DP"
        expected_output = b"Hello"
        self.assertEqual(self.base32.decode(input_data), expected_output)

    def test_encode_with_padding(self):
        """
        Test encoding with input that requires padding.
        """
        input_data = b"Hello, World!"
        expected_output = "JBSWY3DPFQQFO33SNRSCC==="
        self.assertEqual(self.base32.encode(input_data), expected_output)

    def test_decode_with_padding(self):
        """
        Test decoding with input that includes padding.
        """
        input_data = "JBSWY3DPFQQFO33SNRSCC==="
        expected_output = b"Hello, World!"
        self.assertEqual(self.base32.decode(input_data), expected_output)

    def test_encode_decode_roundtrip(self):
        """
        Test encoding and decoding roundtrip to ensure consistency.
        """
        input_data = b"Base32 Test"
        encoded = self.base32.encode(input_data)
        decoded = self.base32.decode(encoded)
        self.assertEqual(decoded, input_data)

    def test_decode_invalid_characters(self):
        """
        Test decoding with invalid characters. Expect a ValueError to be raised.
        """
        input_data = "JBSWY3DPFQQFO33SNRSCC===!"
        with self.assertRaises(ValueError):
            self.base32.decode(input_data)

    def test_encode_special_characters(self):
        """
        Test encoding with special characters in the input.
        """
        input_data = b"Special!@#"
        expected_output = "KNYGKY3JMFWCCQBD"
        self.assertEqual(self.base32.encode(input_data), expected_output)

    def test_decode_special_characters(self):
        """
        Test decoding with special characters in the Base32 string.
        """
        input_data = "KNYGKY3JMFWCCQBD"
        expected_output = b"Special!@#"
        self.assertEqual(self.base32.decode(input_data), expected_output)

    def test_encode_large_input(self):
        """
        Test encoding with a large input to ensure performance and correctness.
        """
        input_data = b"a" * 1000  # 1000 bytes of 'a'
        encoded = self.base32.encode(input_data)
        # Verify that the encoded output is correct by decoding it
        decoded = self.base32.decode(encoded)
        self.assertEqual(decoded, input_data)

    def test_decode_large_input(self):
        """
        Test decoding with a large Base32 string to ensure performance and correctness.
        """
        input_data = "MF" * 1000  # 1000 repetitions of 'MF'
        decoded = self.base32.decode(input_data)
        # Verify that the decoded output is correct by encoding it
        encoded = self.base32.encode(decoded)
        self.assertEqual(encoded, input_data)


if __name__ == "__main__":
    unittest.main()
