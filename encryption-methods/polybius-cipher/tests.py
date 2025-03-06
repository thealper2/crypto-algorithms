import unittest
from polybius_cipher import PolybiusCipher


class TestPolybiusCipher(unittest.TestCase):
    """
    Tests the encryption and decryption functionality of the PolybiusCipher class.
    """

    def setUp(self):
        """
        Generates a PolybiusCipher sample before each test.
        """
        self.polybius = PolybiusCipher()

    def test_create_polybius_square(self):
        """
        Test the correct construction of the Polybius square.
        """
        square, coordinates = self.polybius._create_polybius_square()

        # There must be 25 letters in the square (I and J in the same cell)
        self.assertEqual(len(square), 25)
        self.assertEqual(len(coordinates), 25)

        # Check the coordinates of some letters
        self.assertEqual(square["A"], (1, 1))
        self.assertEqual(square["Z"], (5, 5))
        self.assertEqual(coordinates[(1, 1)], "A")
        self.assertEqual(coordinates[(5, 5)], "Z")

    def test_encrypt(self):
        """
        Tests that the encryption process works correctly.
        """
        # A simple text
        self.assertEqual(self.polybius.encrypt("HELLO"), "2315313134")
        # The letter ‘J’ should be changed to ‘I’
        self.assertEqual(self.polybius.encrypt("hello"), "2315313134")
        # Case insensitivity
        self.assertEqual(self.polybius.encrypt("JELLY"), "2415313154")
        # Spacing and punctuation marks
        self.assertEqual(
            self.polybius.encrypt("HELLO WORLD!"), "2315313134 5234423114!"
        )

    def test_decrypt(self):
        """
        Tests that the decryption process works correctly.
        """
        # A simple ciphertext
        self.assertEqual(self.polybius.decrypt("2315313134"), "HELLO")
        # Spacing and punctuation marks
        self.assertEqual(
            self.polybius.decrypt("2315313134 5234423114!"), "HELLO WORLD!"
        )
        # Invalid characters (decryption should leave them as they are)
        self.assertEqual(self.polybius.decrypt("2315@313134"), "HE@LLO")

    def test_encrypt_decrypt_consistency(self):
        """
        Tests that encryption and decryption are consistent.
        """
        original_text = "HELLO WORLD"
        encrypted_text = self.polybius.encrypt(original_text)
        decrypted_text = self.polybius.decrypt(encrypted_text)
        self.assertEqual(decrypted_text, original_text.replace("J", "I"))

    def test_invalid_characters(self):
        """
        Tests that errors related to invalid characters are correctly caught.
        """
        # Invalid character during encryption
        with self.assertRaises(ValueError):
            self.polybius.encrypt("HELLO123")

        # Invalid coordinates during decryption
        with self.assertRaises(ValueError):
            self.polybius.decrypt("63")

    def test_edge_cases(self):
        """
        Tests edge cases.
        """
        # Blank text
        self.assertEqual(self.polybius.encrypt(""), "")
        self.assertEqual(self.polybius.decrypt(""), "")

        # Spacing and punctuation only
        self.assertEqual(self.polybius.encrypt(" !@#"), " !@#")
        self.assertEqual(self.polybius.decrypt(" !@#"), " !@#")


if __name__ == "__main__":
    unittest.main()
