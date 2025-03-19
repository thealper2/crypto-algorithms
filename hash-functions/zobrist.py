import random
from typing import List


class ZobristHashing:
    """
    Zobrist Hashing implementation for board game states.
    """

    def __init__(self, board_size: int, num_pieces: int):
        """
        Initialize the Zobrist Hashing class.

        Args:
            board_size (int): The size of the board (number of squares).
            num_pieces (int): The number of different pieces (including empty squares).
        """
        if board_size <= 0 or num_pieces <= 0:
            raise ValueError("Board size and number of pieces must be greater than 0.")

        self.board_size = board_size
        self.num_pieces = num_pieces
        self.zobrist_table = self._initialize_zobrist_table()

    def _initialize_zobrist_table(self) -> List[List[int]]:
        """
        Initialize the Zobrist table with random numbers.

        Returns:
            List[List[int]]: A 2D list containing random numbers for each square and piece.
        """
        return [
            [random.getrandbits(64) for _ in range(self.num_pieces)]
            for _ in range(self.board_size)
        ]

    def compute_hash(self, board_state: List[int]) -> int:
        """
        Compute the Zobrist hash for a given board state.

        Args:
            board_state (List[int]): A list representing the current state of the board. Each element corresponds to a piece on the board.

        Returns:
            int: The computed hash value.
        """
        if len(board_state) != self.board_size:
            raise ValueError("Board state length does not match the board size.")

        hash_value = 0
        for square, piece in enumerate(board_state):
            if piece < 0 or piece >= self.num_pieces:
                raise ValueError(f"Invalid piece value {piece} at square {square}.")
            hash_value ^= self.zobrist_table[square][piece]
        return hash_value
