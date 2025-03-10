from typing import List


class LuhnAlgorithm:
    """
    A class to implement the Luhn Algorithm for validating identification numbers such as credit card numbers.
    """

    def __init__(self, number: str):
        """
        Initialize the LuhnAlgorithm class with the number to be validated.

        Args:
            number (str): The number to validate using the Luhn Algorithm.
        """
        self.number = number

    def _clean_input(self) -> List[int]:
        """
        Clean the input by removing any non-digit characters and convert it to a list of integers.

        Returns:
            List[int]: A list of integers representing the cleaned number.

        Raises:
            ValueError: If the input contains non-digit characters after cleaning.
        """
        cleaned = "".join(filter(str.isdigit, self.number))
        if not cleaned:
            raise ValueError("Input must contain at least one digit.")

        return [int(digit) for digit in cleaned]

    def _double_alternate_digits(self, digits: List[int]) -> List[int]:
        """
        Double every second digit starting from the right.

        Args:
            digits (List[int]): List of digits to process.

        Returns:
            List[int]: List of digits with every second digit doubled.
        """
        for i in range(len(digits) - 2, -1, -2):
            digits[i] *= 2
            if digits[i] > 9:
                digits[i] = digits[i] - 9

        return digits

    def _calculate_checksum(eslf, digits: List[int]) -> int:
        """
        Calculate the checksum of the digits.

        Args:
           digits (List[int]): List of digits to calculate the checksum for.

        Returns:
            int: The checksum value.
        """
        return sum(digits)

    def is_valid(self) -> bool:
        """
        Validate the number using the Luhn Algorithm.

        Returns:
            bool: True if the number is valid, False otherwise.

        Raises:
            ValueError: If the input is invalid or empty.
        """
        try:
            digits = self._clean_input()
            digits = self._double_alternate_digits(digits)
            checksum = self._calculate_checksum(digits)
            return checksum % 10 == 0
        except ValueError as e:
            raise ValueError(f"Invalid input: {e}")
