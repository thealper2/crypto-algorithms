import unittest
from row_column import RowColumnCipher


class TestRowColumnCipher(unittest.TestCase):
    """
    Test cases for the RowColumnCipher class.
    """

    def test_encrypt_normal_case(self):
        """
        Test encryption with a normal case.
        """
        cipher = RowColumnCipher("HELLOWORLD", 3)
        encrypted_text = cipher.encrypt()
        self.assertEqual(encrypted_text, "HLODEORXLWLX")  # Expected encrypted text

    def test_decrypt_normal_case(self):
        """
        Test decryption with a normal case.
        """
        cipher = RowColumnCipher("HLODEORXLWLX", 3)
        decrypted_text = cipher.decrypt("HLODEORXLWLX")
        self.assertEqual(decrypted_text, "HELLOWORLD")  # Expected decrypted text

    def test_encrypt_with_padding(self):
        """
        Test encryption when padding is required.
        """
        cipher = RowColumnCipher("HELLO", 4)
        encrypted_text = cipher.encrypt()
        self.assertEqual(
            encrypted_text, "HOEXLXLX"
        )  # Expected encrypted text with padding

    def test_decrypt_with_padding(self):
        """
        Test decryption when padding was added during encryption.
        """
        cipher = RowColumnCipher("HOEXLXLX", 4)
        decrypted_text = cipher.decrypt("HOEXLXLX")
        self.assertEqual(
            decrypted_text, "HELLO"
        )  # Expected decrypted text without padding

    def test_encrypt_empty_string(self):
        """
        Test encryption with an empty string.
        """
        cipher = RowColumnCipher("", 3)
        encrypted_text = cipher.encrypt()
        self.assertEqual(encrypted_text, "")  # Expected empty string

    def test_decrypt_empty_string(self):
        """
        Test decryption with an empty string.
        """
        cipher = RowColumnCipher("", 3)
        decrypted_text = cipher.decrypt("")
        self.assertEqual(decrypted_text, "")  # Expected empty string

    def test_encrypt_single_column(self):
        """
        Test encryption with a single column (no transposition).
        """
        cipher = RowColumnCipher("HELLO", 1)
        encrypted_text = cipher.encrypt()
        self.assertEqual(encrypted_text, "HELLO")  # Expected same as input

    def test_decrypt_single_column(self):
        """
        Test decryption with a single column (no transposition).
        """
        cipher = RowColumnCipher("HELLO", 1)
        decrypted_text = cipher.decrypt("HELLO")
        self.assertEqual(decrypted_text, "HELLO")  # Expected same as input

    def test_encrypt_invalid_column_count(self):
        """
        Test encryption with an invalid column count (zero or negative).
        """
        with self.assertRaises(
            ValueError
        ):  # Expecting a ValueError for invalid column count
            cipher = RowColumnCipher("HELLO", 0)
            cipher.encrypt()

    def test_decrypt_invalid_column_count(self):
        """
        Test decryption with an invalid column count (zero or negative).
        """
        with self.assertRaises(
            ValueError
        ):  # Expecting a ValueError for invalid column count
            cipher = RowColumnCipher("HELLO", -1)
            cipher.decrypt("HELLO")

    def test_encrypt_non_string_input(self):
        """
        Test encryption with non-string input.
        """
        with self.assertRaises(TypeError):  # Expecting a TypeError for non-string input
            cipher = RowColumnCipher(123, 3)
            cipher.encrypt()

    def test_decrypt_non_string_input(self):
        """
        Test decryption with non-string input.
        """
        with self.assertRaises(TypeError):  # Expecting a TypeError for non-string input
            cipher = RowColumnCipher(123, 3)
            cipher.decrypt(123)


if __name__ == "__main__":
    unittest.main()
