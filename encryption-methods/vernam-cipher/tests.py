import unittest
from vernam_cipher import VernamCipher


class TestVernamCipher(unittest.TestCase):
    """
    A test suite for the VernamCipher class.
    This suite tests the encryption and decryption functionality of the Vernam Cipher algorithm.
    """

    def setUp(self):
        """
        Set up the VernamCipher instance to be used in all test cases.
        """
        self.cipher = VernamCipher()

    def test_encrypt_valid_input(self):
        """
        Test encryption with valid plaintext and key of the same length.
        """
        plaintext = "hello"
        key = "world"
        ciphertext = self.cipher.encrypt(plaintext, key)
        # Ensure the ciphertext is a binary string
        self.assertTrue(all(bit in ("0", "1") for bit in ciphertext))

    def test_decrypt_valid_input(self):
        """
        Test decryption with valid ciphertext and key of the same length.
        """
        ciphertext = "0001100001000100100000110"  # Example binary ciphertext
        key = "world"
        plaintext = self.cipher.decrypt(ciphertext, key)
        # Ensure the decrypted plaintext is a string
        self.assertIsInstance(plaintext, str)

    def test_encrypt_decrypt_round_trip(self):
        """
        Test that encrypting and then decrypting returns the original plaintext.
        """
        plaintext = "hello"
        key = "world"
        ciphertext = self.cipher.encrypt(plaintext, key)
        decrypted_text = self.cipher.decrypt(ciphertext, key)
        self.assertEqual(plaintext, decrypted_text)

    def test_encrypt_invalid_key_length(self):
        """
        Test encryption with a key that is not the same length as the plaintext.
        """
        plaintext = "hello"
        key = "short"  # Key is shorter than plaintext
        with self.assertRaises(ValueError):
            self.cipher.encrypt(plaintext, key)

    def test_decrypt_invalid_key_length(self):
        """
        Test decryption with a key that is not the same length as the ciphertext.
        """
        ciphertext = "0001100001000100100000110000"  # Example binary ciphertext
        key = "short"  # Key is shorter than ciphertext
        with self.assertRaises(ValueError):
            self.cipher.decrypt(ciphertext, key)

    def test_encrypt_empty_input(self):
        """
        Test encryption with empty plaintext and key.
        """
        plaintext = ""
        key = ""
        ciphertext = self.cipher.encrypt(plaintext, key)
        self.assertEqual(ciphertext, "")

    def test_decrypt_empty_input(self):
        """
        Test decryption with empty ciphertext and key.
        """
        ciphertext = ""
        key = ""
        plaintext = self.cipher.decrypt(ciphertext, key)
        self.assertEqual(plaintext, "")

    def test_encrypt_non_ascii_input(self):
        """
        Test encryption with non-ASCII characters in plaintext and key.
        """
        plaintext = "こんにちは"  # Japanese characters
        key = "キー"  # Japanese key
        ciphertext = self.cipher.encrypt(plaintext, key)
        # Ensure the ciphertext is a binary string
        self.assertTrue(all(bit in ("0", "1") for bit in ciphertext))

    def test_decrypt_non_ascii_input(self):
        """
        Test decryption with non-ASCII characters in ciphertext and key.
        """
        ciphertext = "1100001010101010111000110"  # Example binary ciphertext
        key = "キー"  # Japanese key
        plaintext = self.cipher.decrypt(ciphertext, key)
        # Ensure the decrypted plaintext is a string
        self.assertIsInstance(plaintext, str)


if __name__ == "__main__":
    unittest.main()
