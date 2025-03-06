import unittest
from bifid_cipher import BifidCipher

class TestBifidCipher(unittest.TestCase):
    """
    Test suite for the BifidCipher class.
    """

    def test_create_polybius_square(self):
        """
        Test the creation of the Polybius square with a given key.
        """
        key = "KEYWORD"
        bifid = BifidCipher(key)

        # Expected 5x5 Polybius square for the key "KEYWORD"
        expected_square = [
            ["K", "E", "Y", "W", "O"],
            ["R", "D", "A", "B", "C"],
            ["F", "G", "H", "I", "L"],
            ["M", "N", "P", "Q", "S"],
            ["T", "U", "V", "X", "Z"],
        ]

        # Expected positions for the characters in the square
        expected_positions = {
            "K": (0, 0),
            "E": (0, 1),
            "Y": (0, 2),
            "W": (0, 3),
            "O": (0, 4),
            "R": (1, 0),
            "D": (1, 1),
            "A": (1, 2),
            "B": (1, 3),
            "C": (1, 4),
            "F": (2, 0),
            "G": (2, 1),
            "H": (2, 2),
            "I": (2, 3),
            "L": (2, 4),
            "M": (3, 0),
            "N": (3, 1),
            "P": (3, 2),
            "Q": (3, 3),
            "S": (3, 4),
            "T": (4, 0),
            "U": (4, 1),
            "V": (4, 2),
            "X": (4, 3),
            "Z": (4, 4),
        }

        # Assert that the generated square and positions match the expected values
        self.assertEqual(bifid.square, expected_square)
        self.assertEqual(bifid.positions, expected_positions)

    def test_encrypt(self):
        """
        Test the encryption functionality of the BifidCipher.
        """
        key = "KEYWORD"
        bifid = BifidCipher(key)

        # Test encryption of a plaintext
        plaintext = "HELLO"
        expected_ciphertext = "FHYCZ"
        ciphertext = bifid.encrypt(plaintext)

        # Assert that the encrypted text matches the expected ciphertext
        self.assertEqual(ciphertext, expected_ciphertext)

    def test_decrypt(self):
        """
        Test the decryption functionality of the BifidCipher.
        """
        key = "KEYWORD"
        bifid = BifidCipher(key)

        # Test decryption of a ciphertext
        ciphertext = "FHYCZ"
        expected_plaintext = "HELLO"
        plaintext = bifid.decrypt(ciphertext)

        # Assert that the decrypted text matches the expected plaintext
        self.assertEqual(plaintext, expected_plaintext)

    def test_encrypt_with_invalid_characters(self):
        """
        Test encryption with plaintext containing characters not in the Polybius square.
        """
        key = "KEYWORD"
        bifid = BifidCipher(key)

        # Test encryption with invalid characters
        plaintext = "HELLO123"

        # Assert that a ValueError is raised for invalid characters
        with self.assertRaises(ValueError):
            bifid.encrypt(plaintext)

    def test_decrypt_with_invalid_characters(self):
        """
        Test decryption with ciphertext containing characters not in the Polybius square.
        """
        key = "KEYWORD"
        bifid = BifidCipher(key)

        # Test decryption with invalid characters
        ciphertext = "DACGF123"

        # Assert that a ValueError is raised for invalid characters
        with self.assertRaises(ValueError):
            bifid.decrypt(ciphertext)

    def test_encrypt_decrypt_consistency(self):
        """
        Test that encrypting and then decrypting a message returns the original plaintext.
        """
        key = "KEYWORD"
        bifid = BifidCipher(key)

        # Test encryption and decryption consistency
        plaintext = "TESTMESSAGE"
        ciphertext = bifid.encrypt(plaintext)
        decrypted_text = bifid.decrypt(ciphertext)

        # Assert that the decrypted text matches the original plaintext
        self.assertEqual(decrypted_text, plaintext)


if __name__ == "__main__":
    unittest.main()
