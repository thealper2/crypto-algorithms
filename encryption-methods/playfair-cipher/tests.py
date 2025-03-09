import unittest
from playfair_cipher import PlayfairCipher


class TestPlayfairCipher(unittest.TestCase):
    """
    A test class for the PlayfairCipher implementation.
    """

    def test_generate_square(self):
        """
        Test the _generate_square method to ensure it creates a valid 5x5 Playfair square.
        """
        cipher = PlayfairCipher("MONARCHY")
        expected_square = [
            ["M", "O", "N", "A", "R"],
            ["C", "H", "Y", "B", "D"],
            ["E", "F", "G", "I", "K"],
            ["L", "P", "Q", "S", "T"],
            ["U", "V", "W", "X", "Z"],
        ]
        self.assertEqual(
            cipher.square,
            expected_square,
            "Generated square does not match the expected square.",
        )

    def test_prepare_text(self):
        """
        Test the _prepare_text method to ensure it correctly prepares the input text.
        """
        cipher = PlayfairCipher("MONARCHY")
        # Test with duplicate letters and odd-length text
        self.assertEqual(
            cipher._prepare_text("HELLO"),
            "HELXLO",
            "Text preparation failed for 'HELLO'.",
        )
        # Test with 'J' replacement
        self.assertEqual(
            cipher._prepare_text("JELLY"),
            "IELLY",
            "Text preparation failed for 'JELLY'.",
        )
        # Test with even-length text
        self.assertEqual(
            cipher._prepare_text("WORLD"),
            "WORLD",
            "Text preparation failed for 'WORLD'.",
        )

    def test_encrypt(self):
        """
        Test the encrypt method to ensure it correctly encrypts the plaintext.
        """
        cipher = PlayfairCipher("MONARCHY")
        # Test basic encryption
        self.assertEqual(
            cipher.encrypt("HELLO"), "DONER", "Encryption failed for 'HELLO'."
        )
        # Test with spaces and special characters (should be ignored or handled)
        self.assertEqual(
            cipher.encrypt("HELLO WORLD"),
            "DONERZWRH",
            "Encryption failed for 'HELLO WORLD'.",
        )
        # Test with 'J' replacement
        self.assertEqual(
            cipher.encrypt("JELLY"), "IEKYK", "Encryption failed for 'JELLY'."
        )

    def test_decrypt(self):
        """
        Test the decrypt method to ensure it correctly decrypts the ciphertext.
        """
        cipher = PlayfairCipher("MONARCHY")
        # Test basic decryption
        self.assertEqual(
            cipher.decrypt("DONER"), "HELXLO", "Decryption failed for 'DONER'."
        )
        # Test with spaces and special characters (should be ignored or handled)
        self.assertEqual(
            cipher.decrypt("DONERZWRH"),
            "HELXLOXWORLD",
            "Decryption failed for 'DONERZWRH'.",
        )
        # Test with 'J' replacement
        self.assertEqual(
            cipher.decrypt("IEKYK"), "IELLY", "Decryption failed for 'IEKYK'."
        )

    def test_find_position(self):
        """
        Test the _find_position method to ensure it correctly locates characters in the Playfair square.
        """
        cipher = PlayfairCipher("MONARCHY")
        # Test valid characters
        self.assertEqual(
            cipher._find_position("M"), (0, 0), "Position of 'M' is incorrect."
        )
        self.assertEqual(
            cipher._find_position("Z"), (4, 4), "Position of 'Z' is incorrect."
        )
        # Test invalid character
        with self.assertRaises(
            ValueError, msg="Expected ValueError for invalid character."
        ):
            cipher._find_position("J")

    def test_edge_cases(self):
        """
        Test edge cases such as empty input, non-alphabetic characters, and invalid keys.
        """
        cipher = PlayfairCipher("MONARCHY")
        # Test empty input
        self.assertEqual(cipher.encrypt(""), "", "Encryption failed for empty input.")
        self.assertEqual(cipher.decrypt(""), "", "Decryption failed for empty input.")
        # Test non-alphabetic characters
        self.assertEqual(
            cipher.encrypt("123!@#"), "", "Encryption failed for non-alphabetic input."
        )
        self.assertEqual(
            cipher.decrypt("123!@#"), "", "Decryption failed for non-alphabetic input."
        )
        # Test invalid key (non-alphabetic)
        with self.assertRaises(ValueError, msg="Expected ValueError for invalid key."):
            PlayfairCipher("123!@#")


if __name__ == "__main__":
    unittest.main()
