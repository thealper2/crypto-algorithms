import unittest
from rot5 import ROT5Cipher


class TestROT5Cipher(unittest.TestCase):
    """
    A test class for the ROT5Cipher implementation.
    """

    def setUp(self):
        """
        Set up the ROT5Cipher instance for testing.
        """
        self.cipher = ROT5Cipher()

    def test_encrypt_digits(self):
        """
        Test encryption of a string containing only digits.
        """
        self.assertEqual(self.cipher.encrypt("12345"), "67890")
        self.assertEqual(self.cipher.encrypt("67890"), "12345")
        self.assertEqual(self.cipher.encrypt("00000"), "55555")
        self.assertEqual(self.cipher.encrypt("99999"), "44444")

    def test_decrypt_digits(self):
        """
        Test decryption of a string containing only digits.
        """
        self.assertEqual(self.cipher.decrypt("67890"), "12345")
        self.assertEqual(self.cipher.decrypt("12345"), "67890")
        self.assertEqual(self.cipher.decrypt("55555"), "00000")
        self.assertEqual(self.cipher.decrypt("44444"), "99999")

    def test_encrypt_mixed_characters(self):
        """
        Test encryption of a string containing mixed characters (digits and non-digits).
        """
        self.assertEqual(self.cipher.encrypt("abc123"), "abc678")
        self.assertEqual(self.cipher.encrypt("1a2b3c"), "6a7b8c")
        self.assertEqual(self.cipher.encrypt("!@#456"), "!@#901")

    def test_decrypt_mixed_characters(self):
        """
        Test decryption of a string containing mixed characters (digits and non-digits).
        """
        self.assertEqual(self.cipher.decrypt("abc678"), "abc123")
        self.assertEqual(self.cipher.decrypt("6a7b8c"), "1a2b3c")
        self.assertEqual(self.cipher.decrypt("!@#901"), "!@#456")

    def test_encrypt_empty_string(self):
        """
        Test encryption of an empty string.
        """
        self.assertEqual(self.cipher.encrypt(""), "")

    def test_decrypt_empty_string(self):
        """
        Test decryption of an empty string.
        """
        self.assertEqual(self.cipher.decrypt(""), "")

    def test_rotate_digit_invalid_input(self):
        """
        Test the _rotate_digit method with invalid input (non-digit or multi-character input).
        """
        with self.assertRaises(ValueError):
            self.cipher._rotate_digit("a")  # Non-digit input
        with self.assertRaises(ValueError):
            self.cipher._rotate_digit("12")  # Multi-character input

    def test_rotate_digit_valid_input(self):
        """
        Test the _rotate_digit method with valid input (single digit).
        """
        self.assertEqual(self.cipher._rotate_digit("0"), "5")
        self.assertEqual(self.cipher._rotate_digit("5"), "0")
        self.assertEqual(self.cipher._rotate_digit("9"), "4")


if __name__ == "__main__":
    unittest.main()
