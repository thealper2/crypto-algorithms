from typing import Union


class VerhoeffAlgorithm:
    """
    A class to implement the Verhoeff Algorithm for checksum validation.

    Attributes:
        _multiplication_table (List[List[int]]): A multiplication table for the dihedral group D5.
        _permutation_table (List[List[int]]): A permutation table for cyclic permutations.
        _inverse_table (List[int]): An inverse table for the dihedral group D5.
    """

    def __init__(self) -> None:
        """
        Initializes the VerhoeffAlgorithm class with precomputed tables.
        """
        # Multiplication table for the dihedral group D5
        self._multiplication_table = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
            [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
            [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
            [4, 0, 1, 2, 3, 9, 5, 6, 7, 8],
            [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
            [6, 5, 9, 8, 7, 1, 0, 4, 3, 2],
            [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
            [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
            [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        ]

        # Permutation table for cyclic permutations
        self._permutation_table = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
            [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
            [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
            [9, 4, 5, 3, 1, 2, 6, 8, 7, 0],
            [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
            [2, 7, 9, 3, 8, 0, 6, 4, 1, 5],
            [7, 0, 4, 6, 9, 1, 3, 2, 5, 8],
        ]

        # Inverse table for the dihedral group D5
        self._inverse_table = [0, 4, 3, 2, 1, 5, 6, 7, 8, 9]

    def _permute(self, num: int, permutation: int) -> int:
        """
        Applies a permutation to a digit based on the permutation table.

        Args:
            num (int): The digit to permute.
            permutation (int): The permutation index.

        Returns:
            int: The permuted digit.
        """
        return self._permutation_table[permutation % 8][num]

    def _multiply(self, x: int, y: int) -> int:
        """
        Multiplies two digits using the multiplication table.

        Args:
            x (int): The first digit.
            y (int): The second digit.

        Returns:
            int: The result of the multiplication.
        """
        return self._multiplication_table[x][y]

    def compute_checksum(self, number: Union[str, int]) -> int:
        """
        Computes the Verhoeff checksum for a given number.

        Args:
            number (Union[str, int]): The number to compute the checksum for.

        Returns:
            int: The computed checksum digit.

        Raises:
            ValueError: If the input is not a valid number.
        """
        if isinstance(number, int):
            number = str(number)

        if not number.isdigit():
            raise ValueError("Input must be a valid number.")

        checksum = 0
        for i, char in enumerate(reversed(number)):
            digit = int(char)
            checksum = self._multiply(checksum, self._permute(digit, i + 1))

        return self._inverse_table[checksum]

    def validate_number(self, number: Union[str, int]) -> bool:
        """
        Validates a number using the Verhoeff checksum.

        Args:
            number (Union[str, int]): The number to validate.

        Returns:
            bool: True if the number is valid, False otherwise.

        Raises:
            ValueError: If the input is not a valid number.
        """
        if isinstance(number, int):
            number = str(number)

        if not number.isdigit():
            raise ValueError("Input must be a valid number.")

        checksum = 0
        for i, char in enumerate(reversed(number)):
            digit = int(char)
            checksum = self._multiply(checksum, self._permute(digit, i))

        return checksum == 0
