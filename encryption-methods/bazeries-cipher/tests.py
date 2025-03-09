import unittest
from bazeries_cipher import (
    BazeriesCipher,
)  # Assuming the BazeriesCipher class is in a file named bazeries_cipher.py


class TestBazeriesCipher(unittest.TestCase):
    """
    A test class for the BazeriesCipher implementation.
    """

    def test_encrypt_valid_input(self):
        """
        Test encryption with valid input.
        """
        cipher = BazeriesCipher(key=123)
        plaintext = "HELLO"
        encrypted_text = cipher.encrypt(plaintext)
        self.assertNotEqual(
            plaintext, encrypted_text
        )  # Encrypted text should not match plaintext
        self.assertIsInstance(encrypted_text, str)  # Encrypted text should be a string

    def test_decrypt_valid_input(self):
        """
        Test decryption with valid input.
        """
        cipher = BazeriesCipher(key=123)
        ciphertext = "AEXHE "  # Example ciphertext (assuming encryption shifts 'HELLO' to 'KHOOR')
        decrypted_text = cipher.decrypt(ciphertext)
        self.assertEqual(
            decrypted_text, "HELLO"
        )  # Decrypted text should match the original plaintext

    def test_encrypt_decrypt_roundtrip(self):
        """
        Test that encrypting and then decrypting returns the original text.
        """
        cipher = BazeriesCipher(key=456)
        plaintext = "PYTHON"
        encrypted_text = cipher.encrypt(plaintext)
        decrypted_text = cipher.decrypt(encrypted_text)
        self.assertEqual(
            plaintext, decrypted_text
        )  # Roundtrip should return the original text

    def test_encrypt_empty_text(self):
        """
        Test encryption with empty text (should raise an error).
        """
        cipher = BazeriesCipher(key=789)
        with self.assertRaises(ValueError):  # Empty text should raise a ValueError
            cipher.encrypt("")

    def test_decrypt_empty_text(self):
        """
        Test decryption with empty text (should raise an error).
        """
        cipher = BazeriesCipher(key=789)
        with self.assertRaises(ValueError):  # Empty text should raise a ValueError
            cipher.decrypt("")

    def test_invalid_key(self):
        """
        Test initialization with an invalid key (non-positive integer).
        """
        with self.assertRaises(
            ValueError
        ):  # Non-positive key should raise a ValueError
            BazeriesCipher(key=0)
        with self.assertRaises(ValueError):  # Negative key should raise a ValueError
            BazeriesCipher(key=-123)

    def test_non_alpha_characters(self):
        """
        Test encryption and decryption with non-alphabetic characters.
        """
        cipher = BazeriesCipher(key=123)
        plaintext = "HELLO 123!"
        encrypted_text = cipher.encrypt(plaintext)
        decrypted_text = cipher.decrypt(encrypted_text)
        self.assertEqual(
            plaintext, decrypted_text
        )  # Non-alphabetic characters should remain unchanged

    def test_large_key(self):
        """
        Test encryption and decryption with a large key.
        """
        cipher = BazeriesCipher(key=999999)
        plaintext = "TESTING"
        encrypted_text = cipher.encrypt(plaintext)
        decrypted_text = cipher.decrypt(encrypted_text)
        self.assertEqual(plaintext, decrypted_text)  # Large key should work correctly

    def test_special_characters(self):
        """
        Test encryption and decryption with special characters.
        """
        cipher = BazeriesCipher(key=123)
        plaintext = "HELLO!@#$%^&*()"
        encrypted_text = cipher.encrypt(plaintext)
        decrypted_text = cipher.decrypt(encrypted_text)
        self.assertEqual(
            plaintext, decrypted_text
        )  # Special characters should remain unchanged


if __name__ == "__main__":
    unittest.main()
