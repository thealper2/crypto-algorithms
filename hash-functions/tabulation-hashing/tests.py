import unittest
from tabulation_hashing import TabulationHashing


class TestTabulationHashing(unittest.TestCase):
    """
    A test class for the TabulationHashing implementation.
    """

    def setUp(self):
        """
        Set up the test environment by initializing a TabulationHashing object.
        """
        self.hasher = TabulationHashing(table_size=256, key_size=8)

    def test_valid_key(self):
        """
        Test the hashing function with a valid key.
        """
        key = 12345
        hash_value = self.hasher.hash(key)
        self.assertIsInstance(hash_value, int)
        self.assertGreaterEqual(hash_value, 0)
        self.assertLess(hash_value, 256)

    def test_zero_key(self):
        """
        Test the hashing function with a key of zero.
        """
        key = 0
        hash_value = self.hasher.hash(key)
        self.assertIsInstance(hash_value, int)
        self.assertGreaterEqual(hash_value, 0)
        self.assertLess(hash_value, 256)

    def test_large_key(self):
        """
        Test the hashing function with a large key.
        """
        key = (1 << 64) - 1  # Maximum 64-bit key
        hash_value = self.hasher.hash(key)
        self.assertIsInstance(hash_value, int)
        self.assertGreaterEqual(hash_value, 0)
        self.assertLess(hash_value, 256)

    def test_negative_key(self):
        """
        Test the hashing function with a negative key.
        """
        key = -12345
        with self.assertRaises(ValueError):
            self.hasher.hash(key)

    def test_key_exceeds_max_size(self):
        """
        Test the hashing function with a key that exceeds the maximum allowed size.
        """
        key = 1 << (8 * 8)  # Key size exceeds 8 bytes
        with self.assertRaises(ValueError):
            self.hasher.hash(key)

    def test_random_tables_initialization(self):
        """
        Test if the random tables are initialized correctly.
        """
        self.assertEqual(len(self.hasher.random_tables), 8)  # key_size = 8
        for table in self.hasher.random_tables:
            self.assertEqual(len(table), 256)  # table_size = 256
            for value in table:
                self.assertIsInstance(value, int)
                self.assertGreaterEqual(value, 0)
                self.assertLess(value, 256)

    def test_deterministic_hashing(self):
        """
        Test if the hashing function produces the same output for the same input.
        """
        key = 12345
        hash_value1 = self.hasher.hash(key)
        hash_value2 = self.hasher.hash(key)
        self.assertEqual(hash_value1, hash_value2)

    def test_different_keys_produce_different_hashes(self):
        """
        Test if different keys produce different hash values (with high probability).
        """
        key1 = 12345
        key2 = 67890
        hash_value1 = self.hasher.hash(key1)
        hash_value2 = self.hasher.hash(key2)
        self.assertNotEqual(hash_value1, hash_value2)


if __name__ == "__main__":
    unittest.main()
