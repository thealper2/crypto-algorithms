import unittest
from pearson import PearsonHashing


class TestPearsonHasher(unittest.TestCase):
    """
    Test cases for the PearsonHashing class.
    """

    def test_default_table_hash(self):
        """
        Test the hash function with the default permutation table.
        """
        hasher = PearsonHashing()
        # Test with an empty string
        self.assertEqual(hasher.hash(""), 98)  # First value in the default table
        # Test with a simple string
        self.assertEqual(hasher.hash("hello"), 207)
        # Test with a different string
        self.assertEqual(hasher.hash("world"), 169)

    def test_custom_table_hash(self):
        """
        Test the hash function with a custom permutation table.
        """
        custom_table = list(range(256))  # A simple custom table
        hasher = PearsonHashing(table=custom_table)
        # Test with an empty string
        self.assertEqual(hasher.hash(""), 0)  # First value in the custom table
        # Test with a simple string
        self.assertEqual(hasher.hash("hello"), 104)  # Sum of ASCII values mod 256
        # Test with a different string
        self.assertEqual(hasher.hash("world"), 119)

    def test_invalid_table(self):
        """
        Test the initialization with an invalid permutation table.
        """
        # Table with incorrect length
        with self.assertRaises(ValueError):
            PearsonHashing(table=[1, 2, 3])
        # Table with non-integer values
        with self.assertRaises(ValueError):
            PearsonHashing(table=[1.5, 2.5, 3.5] * 86)  # 258 elements
        # Table with duplicate values
        with self.assertRaises(ValueError):
            PearsonHashing(table=[1] * 256)

    def test_invalid_input_type(self):
        """
        Test the hash function with invalid input types.
        """
        hasher = PearsonHashing()
        # Test with a non-string input
        with self.assertRaises(TypeError):
            hasher.hash(123)  # Integer input
        with self.assertRaises(TypeError):
            hasher.hash([1, 2, 3])  # List input

    def test_edge_cases(self):
        """
        Test edge cases for the hash function.
        """
        hasher = PearsonHashing()
        # Test with a very long string
        long_string = "a" * 1000
        self.assertIsInstance(hasher.hash(long_string), int)
        # Test with special characters
        self.assertEqual(hasher.hash("!@#$%^&*()"), 245)
        # Test with Unicode characters
        self.assertEqual(hasher.hash("こんにちは"), 101)

    def test_hash_consistency(self):
        """
        Test that the hash function produces consistent results for the same input.
        """
        hasher = PearsonHashing()
        message = "consistent"
        hash1 = hasher.hash(message)
        hash2 = hasher.hash(message)
        self.assertEqual(hash1, hash2)


if __name__ == "__main__":
    unittest.main()
