import unittest
from bacon_cipher import BaconCipher


class TestBaconCipher(unittest.TestCase):
    """
    A test class for the BaconCipher implementation.
    """

    def setUp(self) -> None:
        """
        Set up the BaconCipher instance for testing.
        """
        self.cipher = BaconCipher()

    def test_encode_valid_input(self) -> None:
        """
        Test encoding with valid input.
        """
        plaintext = "HELLO"
        expected_ciphertext = "0011100100010100101001101"
        self.assertEqual(self.cipher.encode(plaintext), expected_ciphertext)

    def test_encode_invalid_input(self) -> None:
        """
        Test encoding with invalid input (characters not in the Baconian alphabet).
        """
        plaintext = "HELLO123"
        with self.assertRaises(ValueError):
            self.cipher.encode(plaintext)

    def test_decode_valid_input(self) -> None:
        """
        Test decoding with valid input.
        """
        ciphertext = "0011100100010100101001101"
        expected_plaintext = "HELLO"
        self.assertEqual(self.cipher.decode(ciphertext), expected_plaintext)

    def test_decode_invalid_length(self) -> None:
        """
        Test decoding with invalid input (ciphertext length not a multiple of 5).
        """
        ciphertext = "001110010001010101010011"  # Length is 24, not a multiple of 5
        with self.assertRaises(ValueError):
            self.cipher.decode(ciphertext)

    def test_decode_invalid_binary(self) -> None:
        """
        Test decoding with invalid input (ciphertext contains invalid binary chunks).
        """
        ciphertext = "00111001000101010101001100002"  # "00002" is invalid
        with self.assertRaises(ValueError):
            self.cipher.decode(ciphertext)

    def test_encode_decode_roundtrip(self) -> None:
        """
        Test encoding and decoding roundtrip to ensure consistency.
        """
        plaintext = "SECRET"
        encoded = self.cipher.encode(plaintext)
        decoded = self.cipher.decode(encoded)
        self.assertEqual(decoded, plaintext)

    def test_case_insensitivity(self) -> None:
        """
        Test that encoding is case-insensitive.
        """
        plaintext_lower = "hello"
        plaintext_upper = "HELLO"
        self.assertEqual(
            self.cipher.encode(plaintext_lower), self.cipher.encode(plaintext_upper)
        )


if __name__ == "__main__":
    unittest.main()
