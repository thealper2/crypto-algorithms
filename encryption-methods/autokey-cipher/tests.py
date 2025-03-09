import unittest
from autokey_cipher import AutokeyCipher


class TestAutokeyCipher(unittest.TestCase):
    """
    A test class for the AutokeyCipher implementation.
    """

    def test_encryption(self):
        """
        Test the encryption functionality of the AutokeyCipher.
        """
        cipher = AutokeyCipher("LEMON")
        plaintext = "MONKEY"
        expected_ciphertext = "XSZYRK"
        self.assertEqual(cipher.encrypt(plaintext), expected_ciphertext)

    def test_decryption(self):
        """
        Test the decryption functionality of the AutokeyCipher.
        """
        cipher = AutokeyCipher("LEMON")
        ciphertext = "XSZYRK"
        expected_plaintext = "MONKEY"
        self.assertEqual(cipher.decrypt(ciphertext), expected_plaintext)

    def test_encryption_with_different_key(self):
        """
        Test encryption with a different key to ensure the key is used correctly.
        """
        cipher = AutokeyCipher("KEY")
        plaintext = "HELLO"
        expected_ciphertext = "RIJSS"
        self.assertEqual(cipher.encrypt(plaintext), expected_ciphertext)

    def test_decryption_with_different_key(self):
        """
        Test decryption with a different key to ensure the key is used correctly.
        """
        cipher = AutokeyCipher("KEY")
        ciphertext = "RIJSS"
        expected_plaintext = "HELLO"
        self.assertEqual(cipher.decrypt(ciphertext), expected_plaintext)

    def test_encryption_with_non_alphabetic_plaintext(self):
        """
        Test encryption with non-alphabetic plaintext to ensure it raises a ValueError.
        """
        cipher = AutokeyCipher("LEMON")
        plaintext = "ATTACK123"
        with self.assertRaises(ValueError):
            cipher.encrypt(plaintext)

    def test_decryption_with_non_alphabetic_ciphertext(self):
        """
        Test decryption with non-alphabetic ciphertext to ensure it raises a ValueError.
        """
        cipher = AutokeyCipher("LEMON")
        ciphertext = "LXFOP123"
        with self.assertRaises(ValueError):
            cipher.decrypt(ciphertext)

    def test_encryption_with_empty_plaintext(self):
        """
        Test encryption with empty plaintext to ensure it returns an empty string.
        """
        cipher = AutokeyCipher("LEMON")
        plaintext = ""
        self.assertEqual(cipher.encrypt(plaintext), "")

    def test_decryption_with_empty_ciphertext(self):
        """
        Test decryption with empty ciphertext to ensure it returns an empty string.
        """
        cipher = AutokeyCipher("LEMON")
        ciphertext = ""
        self.assertEqual(cipher.decrypt(ciphertext), "")

    def test_encryption_with_lowercase_plaintext(self):
        """
        Test encryption with lowercase plaintext to ensure it is converted to uppercase.
        """
        cipher = AutokeyCipher("LEMON")
        plaintext = "monkey"
        expected_ciphertext = "XSZYRK"
        self.assertEqual(cipher.encrypt(plaintext), expected_ciphertext)

    def test_decryption_with_lowercase_ciphertext(self):
        """
        Test decryption with lowercase ciphertext to ensure it is converted to uppercase.
        """
        cipher = AutokeyCipher("LEMON")
        ciphertext = "XSZYRK"
        expected_plaintext = "MONKEY"
        self.assertEqual(cipher.decrypt(ciphertext), expected_plaintext)

    def test_initialization_with_non_alphabetic_key(self):
        """
        Test initialization with a non-alphabetic key to ensure it raises a ValueError.
        """
        with self.assertRaises(ValueError):
            AutokeyCipher("LEMON123")


if __name__ == "__main__":
    unittest.main()
