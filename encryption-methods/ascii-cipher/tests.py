import unittest
from ascii_cipher import ASCIICipher


class TestASCIICipher(unittest.TestCase):
    """
    Test cases for the ASCIICipher class.
    """

    def test_encrypt_valid_input(self):
        """
        Test encryption with valid input.
        """
        cipher = ASCIICipher(shift=3)
        result = cipher.encrypt("Hello")
        self.assertEqual(result, "Khoor", "Encryption failed for 'Hello' with shift=3.")

    def test_decrypt_valid_input(self):
        """
        Test decryption with valid input.
        """
        cipher = ASCIICipher(shift=3)
        result = cipher.decrypt("Khoor")
        self.assertEqual(result, "Hello", "Decryption failed for 'Khoor' with shift=3.")

    def test_encrypt_with_uppercase(self):
        """
        Test encryption with uppercase letters.
        """
        cipher = ASCIICipher(shift=4)
        result = cipher.encrypt("WORLD")
        self.assertEqual(result, "[SVPH", "Encryption failed for 'WORLD' with shift=4.")

    def test_decrypt_with_uppercase(self):
        """
        Test decryption with uppercase letters.
        """
        cipher = ASCIICipher(shift=4)
        result = cipher.decrypt("[SVPH")
        self.assertEqual(result, "WORLD", "Decryption failed for '[SVPH' with shift=4.")

    def test_encrypt_with_empty_string(self):
        """
        Test encryption with an empty string.
        """
        cipher = ASCIICipher(shift=5)
        result = cipher.encrypt("")
        self.assertEqual(result, "", "Encryption failed for an empty string.")

    def test_decrypt_with_empty_string(self):
        """
        Test decryption with an empty string.
        """
        cipher = ASCIICipher(shift=5)
        result = cipher.decrypt("")
        self.assertEqual(result, "", "Decryption failed for an empty string.")

    def test_encrypt_with_large_shift(self):
        """
        Test encryption with a shift value larger than 128.
        """
        cipher = ASCIICipher(shift=130)
        result = cipher.encrypt("Test")
        self.assertEqual(result, "Vguv", "Encryption failed for 'Test' with shift=130.")

    def test_decrypt_with_large_shift(self):
        """
        Test decryption with a shift value larger than 128.
        """
        cipher = ASCIICipher(shift=130)
        result = cipher.decrypt("Vguv")
        self.assertEqual(result, "Test", "Decryption failed for 'Vguv' with shift=130.")

    def test_encrypt_with_non_string_input(self):
        """
        Test encryption with non-string input (should raise TypeError).
        """
        cipher = ASCIICipher(shift=3)
        with self.assertRaises(TypeError):
            cipher.encrypt(123)  # Passing an integer instead of a string

    def test_decrypt_with_non_string_input(self):
        """
        Test decryption with non-string input (should raise TypeError).
        """
        cipher = ASCIICipher(shift=3)
        with self.assertRaises(TypeError):
            cipher.decrypt(123)  # Passing an integer instead of a string


if __name__ == "__main__":
    unittest.main()
