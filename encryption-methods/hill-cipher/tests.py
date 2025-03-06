import unittest
import numpy as np
from hill_cipher import HillCipher


class TestHillCipher(unittest.TestCase):
    """
    A test class for the HillCipher implementation.
    """

    def setUp(self):
        """
        Set up the key matrix and HillCipher instance for testing.
        """
        self.key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
        self.hill_cipher = HillCipher(self.key_matrix)

    def test_mod_inverse(self):
        """
        Test the mod_inverse method for valid and invalid inputs.
        """
        # Test valid modular inverse
        self.assertEqual(
            HillCipher.mod_inverse(3, 26), 9, "Modular inverse of 3 mod 26 should be 9"
        )

        # Test invalid modular inverse (no inverse exists)
        self.assertIsNone(
            HillCipher.mod_inverse(2, 26),
            "Modular inverse of 2 mod 26 should not exist",
        )

    def test_encrypt(self):
        """
        Test the encryption method with a known plaintext and key.
        """
        plaintext = "HELLO"
        expected_ciphertext = "JUDDS"  # Expected result for the given key matrix
        encrypted = self.hill_cipher.encrypt(plaintext)
        self.assertEqual(
            encrypted.replace("X", ""),
            expected_ciphertext,
            f"Encryption failed. Expected: {expected_ciphertext}, Got: {encrypted}",
        )

    def test_decrypt(self):
        """
        Test the decryption method with a known ciphertext and key.
        """
        ciphertext = "JUDDS"
        expected_plaintext = "HELLO"  # Expected result for the given key matrix
        decrypted = self.hill_cipher.decrypt(ciphertext)
        self.assertEqual(
            decrypted,
            expected_plaintext,
            f"Decryption failed. Expected: {expected_plaintext}, Got: {decrypted}",
        )

    def test_encrypt_decrypt_consistency(self):
        """
        Test that encrypting and then decrypting a message returns the original message.
        """
        plaintext = "MESSAGE"
        encrypted = self.hill_cipher.encrypt(plaintext)
        decrypted = self.hill_cipher.decrypt(encrypted)
        self.assertEqual(
            decrypted.replace("X", ""),
            plaintext,
            "Encryption and decryption should return the original message",
        )

    def test_invalid_key_matrix(self):
        """
        Test that a non-invertible key matrix raises a ValueError during decryption.
        """
        invalid_key_matrix = np.array([[1, 2], [2, 4]])  # Non-invertible matrix
        hill_cipher_invalid = HillCipher(invalid_key_matrix)
        ciphertext = "JUDDS"

        with self.assertRaises(
            ValueError,
            msg="Decryption with a non-invertible key matrix should raise a ValueError",
        ):
            hill_cipher_invalid.decrypt(ciphertext)

    def test_encrypt_with_padding(self):
        """
        Test that the encryption method correctly pads the plaintext if its length is not a multiple of the key matrix size.
        """
        plaintext = "HELL"  # Length 4, not a multiple of 3 (key matrix size)
        encrypted = self.hill_cipher.encrypt(plaintext)
        # Ensure the encrypted text length is a multiple of the key matrix size
        self.assertEqual(
            len(encrypted) % self.key_matrix.shape[0],
            0,
            "Encrypted text should be padded correctly",
        )

    def test_decrypt_with_padding(self):
        """
        Test that the decryption method correctly handles padded ciphertext.
        """
        ciphertext = "JUDDS"  # Padded ciphertext
        decrypted = self.hill_cipher.decrypt(ciphertext)
        # Ensure the decrypted text does not contain padding characters
        self.assertNotIn(
            "X", decrypted, "Decrypted text should not contain padding characters"
        )


if __name__ == "__main__":
    unittest.main()
