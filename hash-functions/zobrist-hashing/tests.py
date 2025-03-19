import unittest
from zobrist import ZobristHashing


class TestZobristHashing(unittest.TestCase):
    """
    Test cases for the ZobristHashing class.
    """

    def setUp(self):
        """
        Set up a ZobristHashing instance for testing.
        """
        self.board_size = 8
        self.num_pieces = 3
        self.zobrist = ZobristHashing(self.board_size, self.num_pieces)

    def test_valid_board_state(self):
        """
        Test the compute_hash method with a valid board state.
        """
        board_state = [0, 1, 2, 0, 1, 2, 0, 1]  # Valid board state
        hash_value = self.zobrist.compute_hash(board_state)
        self.assertIsInstance(hash_value, int)  # Hash value should be an integer

    def test_invalid_board_size(self):
        """
        Test the compute_hash method with an invalid board state length.
        """
        board_state = [0, 1, 2, 0, 1]  # Invalid length (less than board_size)
        with self.assertRaises(ValueError):
            self.zobrist.compute_hash(board_state)

    def test_invalid_piece_value(self):
        """
        Test the compute_hash method with an invalid piece value.
        """
        board_state = [
            0,
            1,
            3,
            0,
            1,
            2,
            0,
            1,
        ]  # Invalid piece value (3 is out of range)
        with self.assertRaises(ValueError):
            self.zobrist.compute_hash(board_state)

    def test_negative_piece_value(self):
        """
        Test the compute_hash method with a negative piece value.
        """
        board_state = [0, -1, 2, 0, 1, 2, 0, 1]  # Negative piece value
        with self.assertRaises(ValueError):
            self.zobrist.compute_hash(board_state)

    def test_empty_board_state(self):
        """
        Test the compute_hash method with an empty board state.
        """
        board_state = []  # Empty board state
        with self.assertRaises(ValueError):
            self.zobrist.compute_hash(board_state)

    def test_invalid_initialization(self):
        """
        Test the initialization of ZobristHashing with invalid parameters.
        """
        with self.assertRaises(ValueError):
            ZobristHashing(0, 3)  # Invalid board_size
        with self.assertRaises(ValueError):
            ZobristHashing(8, 0)  # Invalid num_pieces

    def test_hash_consistency(self):
        """
        Test that the hash value is consistent for the same board state.
        """
        board_state = [0, 1, 2, 0, 1, 2, 0, 1]
        hash_value1 = self.zobrist.compute_hash(board_state)
        hash_value2 = self.zobrist.compute_hash(board_state)
        self.assertEqual(hash_value1, hash_value2)  # Hash values should be the same

    def test_hash_uniqueness(self):
        """
        Test that different board states produce different hash values.
        """
        board_state1 = [0, 1, 2, 0, 1, 2, 0, 1]
        board_state2 = [0, 1, 2, 0, 1, 2, 0, 2]  # Slightly different board state
        hash_value1 = self.zobrist.compute_hash(board_state1)
        hash_value2 = self.zobrist.compute_hash(board_state2)
        self.assertNotEqual(hash_value1, hash_value2)  # Hash values should be different


if __name__ == "__main__":
    unittest.main()
