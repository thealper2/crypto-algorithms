import unittest
from fsb import FSBHash


class TestFSBHash(unittest.TestCase):
    """Unit tests for the FSBHash class."""

    def setUp(self) -> None:
        """Set up common parameters for tests."""
        self.n = 10
        self.k = 5
        self.t = 3
        self.valid_message = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        self.invalid_message_length = [1, 0, 1]  # Too short
        self.invalid_message_values = [1, 0, 2, 0, 1, 0, 1, 0, 1, 0]  # Contains 2

    def test_initialization_valid(self):
        """Test valid initialization of FSBHash."""
        fsb = FSBHash(self.n, self.k, self.t)
        self.assertEqual(fsb.n, self.n)
        self.assertEqual(fsb.k, self.k)
        self.assertEqual(fsb.t, self.t)
        self.assertEqual(len(fsb.H), self.k)
        for row in fsb.H:
            self.assertEqual(sum(row), self.t)
            self.assertEqual(len(row), self.n)

    def test_initialization_invalid_t(self):
        """Test initialization failure when t is invalid."""
        with self.assertRaises(ValueError):
            FSBHash(self.n, self.k, 0)  # t <= 0
        with self.assertRaises(ValueError):
            FSBHash(self.n, self.k, self.n + 1)  # t > n

    def test_initialization_invalid_k_n(self):
        """Test initialization failure for invalid n and k."""
        with self.assertRaises(ValueError):
            FSBHash(0, self.k, self.t)  # n <= 0
        with self.assertRaises(ValueError):
            FSBHash(self.n, 0, self.t)  # k <= 0

    def test_hash_valid_message(self):
        """Test hashing of a valid binary message."""
        fsb = FSBHash(self.n, self.k, self.t)
        result = fsb.hash(self.valid_message)
        # Output length must equal k
        self.assertEqual(len(result), self.k)
        # Output must contain only 0s and 1s
        for bit in result:
            self.assertIn(bit, (0, 1))

    def test_hash_invalid_message_length(self):
        """Test hash function raises error on invalid message length."""
        fsb = FSBHash(self.n, self.k, self.t)
        with self.assertRaises(ValueError):
            fsb.hash(self.invalid_message_length)

    def test_hash_invalid_message_values(self):
        """Test hash function raises error on non-binary message."""
        fsb = FSBHash(self.n, self.k, self.t)
        with self.assertRaises(ValueError):
            fsb.hash(self.invalid_message_values)

    def test_print_matrix(self):
        """Test if the parity-check matrix prints without errors."""
        fsb = FSBHash(self.n, self.k, self.t)
        try:
            fsb.print_matrix()
        except Exception as e:
            self.fail(f"print_matrix() raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
