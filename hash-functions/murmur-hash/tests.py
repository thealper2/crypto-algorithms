import unittest
from murmur import MurmurHash


class TestMurmurHash(unittest.TestCase):
    """
    Test cases for the MurmurHash implementation.
    """

    def test_hash_string(self):
        """
        Test the MurmurHash3 algorithm with string input.
        """
        murmur = MurmurHash(seed=0)
        # Test with a simple string
        self.assertEqual(murmur.hash("hello"), 613153351)
        # Test with an empty string
        self.assertEqual(murmur.hash(""), 0)
        # Test with a longer string
        self.assertEqual(murmur.hash("MurmurHash"), 986999570)

    def test_hash_bytes(self):
        """
        Test the MurmurHash3 algorithm with bytes input.
        """
        murmur = MurmurHash(seed=0)
        # Test with bytes
        self.assertEqual(murmur.hash(b"hello"), 613153351)
        # Test with empty bytes
        self.assertEqual(murmur.hash(b""), 0)  # Seed value for empty input
        # Test with longer bytes
        self.assertEqual(murmur.hash(b"MurmurHash"), 986999570)

    def test_hash_invalid_input(self):
        """
        Test the MurmurHash3 algorithm with invalid input types.
        """
        murmur = MurmurHash(seed=0)
        # Test with integer input (should raise TypeError)
        with self.assertRaises(TypeError):
            murmur.hash(123)
        # Test with list input (should raise TypeError)
        with self.assertRaises(TypeError):
            murmur.hash([1, 2, 3])

    def test_hash_with_different_seeds(self):
        """
        Test the MurmurHash3 algorithm with different seed values.
        """
        # Test with seed = 0
        murmur1 = MurmurHash(seed=0)
        self.assertEqual(murmur1.hash("test"), 3127628307)
        # Test with seed = 42
        murmur2 = MurmurHash(seed=42)
        self.assertEqual(murmur2.hash("test"), 3959873882)
        # Test with a large seed
        murmur3 = MurmurHash(seed=123456789)
        self.assertEqual(murmur3.hash("test"), 971233694)

    def test_hash_edge_cases(self):
        """
        Test the MurmurHash3 algorithm with edge cases.
        """
        murmur = MurmurHash(seed=0)
        # Test with a string containing special characters
        self.assertEqual(murmur.hash("!@#$%^&*()"), 3947575985)
        # Test with a string containing Unicode characters
        self.assertEqual(murmur.hash("こんにちは"), 757219804)
        # Test with a very long string
        long_string = "a" * 1000
        self.assertEqual(murmur.hash(long_string), 2716186120)


if __name__ == "__main__":
    unittest.main()
