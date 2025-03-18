import unittest
from fletcher import Fletcher


class TestFletcherChecksum(unittest.TestCase):
    """
    A test suite for the FletcherChecksum class.
    """

    def test_compute_checksum_valid_input(self):
        """
        Test the compute_checksum method with valid input.
        """
        data = "Hello, World!"
        fletcher = Fletcher(data)
        checksum = fletcher.compute_checksum()
        self.assertEqual(checksum, 45165)  # Precomputed checksum for "Hello, World!"

    def test_compute_checksum_empty_input(self):
        """
        Test the compute_checksum method with empty input.
        It should raise a ValueError.
        """
        data = ""
        fletcher = Fletcher(data)
        with self.assertRaises(ValueError):
            fletcher.compute_checksum()

    def test_validate_checksum_valid(self):
        """
        Test the validate_checksum method with a valid checksum.
        It should return True.
        """
        data = "Hello, World!"
        checksum = 45165  # Precomputed checksum for "Hello, World!"
        is_valid = Fletcher.validate_checksum(data, checksum)
        self.assertTrue(is_valid)

    def test_validate_checksum_invalid(self):
        """
        Test the validate_checksum method with an invalid checksum.
        It should return False.
        """
        data = "Hello, World!"
        checksum = 12345  # Incorrect checksum
        is_valid = Fletcher.validate_checksum(data, checksum)
        self.assertFalse(is_valid)

    def test_compute_checksum_single_character(self):
        """
        Test the compute_checksum method with a single character input.
        """
        data = "A"
        fletcher = Fletcher(data)
        checksum = fletcher.compute_checksum()
        self.assertEqual(checksum, 16705)  # ASCII value of 'A' is 65

    def test_compute_checksum_large_input(self):
        """
        Test the compute_checksum method with a large input string.
        """
        data = "Python is awesome!"
        fletcher = Fletcher(data)
        checksum = fletcher.compute_checksum()
        self.assertEqual(
            checksum, 24502
        )  # Precomputed checksum for "Python is awesome!"


if __name__ == "__main__":
    unittest.main()
