class DammAlgorithm:
    """
    A class to implement the Damm Algorithm for error detection in numeric codes.

    Attributes:
        quasigroup_table (List(List[int])): A 10x10 quasigroup table used for the algorithm.
    """

    def __init__(self):
        """
        Initializes the DammAlgorithm class with the predefined quasigroup table.
        """
        self.quasigroup_table = [
            [0, 3, 1, 7, 5, 9, 8, 6, 4, 2],
            [7, 0, 9, 2, 1, 5, 4, 8, 6, 3],
            [4, 2, 0, 6, 8, 7, 1, 3, 5, 9],
            [1, 7, 5, 0, 9, 8, 3, 4, 2, 6],
            [6, 1, 2, 3, 0, 4, 5, 9, 7, 8],
            [3, 6, 7, 4, 2, 0, 9, 5, 8, 1],
            [5, 8, 6, 9, 7, 2, 0, 1, 3, 4],
            [8, 9, 4, 5, 3, 6, 2, 0, 1, 7],
            [9, 4, 3, 8, 6, 1, 7, 2, 0, 5],
            [2, 5, 8, 1, 4, 3, 6, 7, 9, 0],
        ]

    def compute_check_digit(self, number: int) -> int:
        """
        Computes the check digit for a given number using the Damm Algorithm.

        Args:
            number (int): The number for which the check digit is to be computed.

        Returns:
            int: The computed check digit.

        Raises:
            ValueError: If the input number is negative.
        """
        if number < 0:
            raise ValueError("Input number must be non-negative.")

        interim = 0
        for digit in str(number):
            interim = self.quasigroup_table[interim][int(digit)]

        return interim

    def validate_number(self, number: int) -> bool:
        """
        Validates a number with its check digit using the Damm Algorithm.

        Args:
            number (int): The number to validate, including the check digit as an last digit.

        Returns:
            bool: True if the number is valid, False otherwise.

        Raises:
            ValueError: If the input number is negative.
        """
        if number < 0:
            raise ValueError("Input number must be non-negative.")

        return self.compute_check_digit(number) == 0
