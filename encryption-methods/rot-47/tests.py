import unittest
from rot47 import ROT47Cipher


class TestROT47Cipher(unittest.TestCase):
    """
    A test class for the ROT47Cipher implementation.
    """

    def setUp(self):
        """
        Set up the ROT47Cipher instance for testing.
        """
        self.cipher = ROT47Cipher()

    def test_encrypt_valid_input(self):
        """
        Test encryption with valid input.
        """
        # Test basic encryption
        self.assertEqual(self.cipher.encrypt("Hello, World!"), "w6==@[ (@C=5P")

    def test_decrypt_valid_input(self):
        """
        Test decryption with valid input.
        """
        # Test basic decryption
        self.assertEqual(self.cipher.decrypt("w6==@[ (@C=5P"), "Hello, World!")

    def test_encrypt_decrypt_inverse(self):
        """
        Test that encryption and decryption are inverses of each other.
        """
        text = "ROT47 is fun!"
        encrypted = self.cipher.encrypt(text)
        decrypted = self.cipher.decrypt(encrypted)
        self.assertEqual(decrypted, text)

    def test_encrypt_invalid_input(self):
        """
        Test encryption with invalid input (non-string).
        """
        with self.assertRaises(ValueError):
            self.cipher.encrypt(123)  # Input is not a string

    def test_edge_cases(self):
        """
        Test edge cases such as empty string and non-printable characters.
        """
        # Test empty string
        self.assertEqual(self.cipher.encrypt(""), "")
        self.assertEqual(self.cipher.decrypt(""), "")
        # Test non-printable ASCII characters
        self.assertEqual(
            self.cipher.encrypt("\x00\x1f"), "\x00\x1f"
        )  # Characters below 33
        self.assertEqual(self.cipher.encrypt("\x7f"), "\x7f")  # Character above 126

    def test_rotate_char_invalid_input(self):
        """
        Test the internal _rotate_char method with invalid input.
        """
        # Test with empty string
        self.assertIsNone(self.cipher._rotate_char(""))
        # Test with multiple characters
        self.assertIsNone(self.cipher._rotate_char("ab"))

    def test_rotate_char_valid_input(self):
        """
        Test the internal _rotate_char method with valid input.
        """
        # Test with a single character
        self.assertEqual(self.cipher._rotate_char("A"), "p")
        # Test with a special character
        self.assertEqual(self.cipher._rotate_char("!"), "P")


if __name__ == "__main__":
    unittest.main()
