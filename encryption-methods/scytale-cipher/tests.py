import unittest
from scytale_cipher import ScytaleCipher


class TestScytaleCipher(unittest.TestCase):
    """
    A test class for the ScytaleCipher implementation.
    """

    def test_encrypt_valid_key(self):
        """
        Test encryption with a valid key.
        """
        cipher = ScytaleCipher(key=3)
        plaintext = "HELLOWORLD"
        expected_ciphertext = "HOLEW DLOLR".replace(" ", "")
        encrypted_text = cipher.encrypt(plaintext)
        self.assertEqual(encrypted_text, expected_ciphertext)

    def test_decrypt_valid_key(self):
        """
        Test decryption with a valid key.
        """
        cipher = ScytaleCipher(key=3)
        ciphertext = "HOLEW DLOLR".replace(" ", "")
        expected_plaintext = "HELLOWORLD"
        decrypted_text = cipher.decrypt(ciphertext)
        self.assertEqual(decrypted_text, expected_plaintext)

    def test_encrypt_decrypt_consistency(self):
        """
        Test that encrypting and then decrypting returns the original plaintext.
        """
        cipher = ScytaleCipher(key=4)
        plaintext = "PYTHONISFUN"
        encrypted_text = cipher.encrypt(plaintext)
        decrypted_text = cipher.decrypt(encrypted_text)
        self.assertEqual(decrypted_text, plaintext)

    def test_encrypt_with_spaces(self):
        """
        Test encryption with spaces in the plaintext.
        Spaces should be removed during encryption.
        """
        cipher = ScytaleCipher(key=2)
        plaintext = "HELLO WORLD"
        expected_ciphertext = "HWEOL RLLOD".replace(" ", "")
        encrypted_text = cipher.encrypt(plaintext)
        self.assertEqual(encrypted_text, expected_ciphertext)

    def test_decrypt_with_spaces(self):
        """
        Test decryption with spaces in the ciphertext.
        Spaces should be removed during decryption.
        """
        cipher = ScytaleCipher(key=2)
        ciphertext = "HWEOL RLLOD".replace(" ", "")
        expected_plaintext = "HELLOWORLD"
        decrypted_text = cipher.decrypt(ciphertext)
        self.assertEqual(decrypted_text, expected_plaintext)

    def test_invalid_key_initialization(self):
        """
        Test that initializing with an invalid key (<= 0) raises a ValueError.
        """
        with self.assertRaises(ValueError):
            ScytaleCipher(key=0)
        with self.assertRaises(ValueError):
            ScytaleCipher(key=-5)

    def test_encrypt_empty_string(self):
        """
        Test encryption with an empty string.
        The result should also be an empty string.
        """
        cipher = ScytaleCipher(key=3)
        plaintext = ""
        encrypted_text = cipher.encrypt(plaintext)
        self.assertEqual(encrypted_text, "")

    def test_decrypt_empty_string(self):
        """
        Test decryption with an empty string.
        The result should also be an empty string.
        """
        cipher = ScytaleCipher(key=3)
        ciphertext = ""
        decrypted_text = cipher.decrypt(ciphertext)
        self.assertEqual(decrypted_text, "")

    def test_encrypt_non_alphabetic_characters(self):
        """
        Test encryption with non-alphabetic characters.
        Non-alphabetic characters should be ignored or handled as per the implementation.
        """
        cipher = ScytaleCipher(key=3)
        plaintext = "HELLO123WORLD!"
        expected_ciphertext = "H1RE2LL3DLW!OO".replace(" ", "")
        encrypted_text = cipher.encrypt(plaintext)
        self.assertEqual(encrypted_text, expected_ciphertext)

    def test_decrypt_non_alphabetic_characters(self):
        """
        Test decryption with non-alphabetic characters.
        Non-alphabetic characters should be ignored or handled as per the implementation.
        """
        cipher = ScytaleCipher(key=3)
        ciphertext = "H1RE2LL3DLW!OO".replace(" ", "")
        expected_plaintext = "HELLOWORLD"
        decrypted_text = cipher.decrypt(ciphertext)
        self.assertEqual(decrypted_text, expected_plaintext)


if __name__ == "__main__":
    unittest.main()
