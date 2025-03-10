import unittest
from luhn_algorithm import LuhnAlgorithm


class TestLuhnAlgorithm(unittest.TestCase):
    """
    A test class for the LuhnAlgorithm implementation.
    """

    def test_valid_numbers(self):
        """
        Test valid numbers that should pass the Luhn Algorithm check.
        """
        valid_numbers = [
            "4532015112830366",  # Valid credit card number
            "6011111111111117",  # Valid credit card number
            "79927398713",  # Valid number
        ]
        for number in valid_numbers:
            luhn = LuhnAlgorithm(number)
            self.assertTrue(luhn.is_valid(), f"Number {number} should be valid.")

    def test_invalid_numbers(self):
        """
        Test invalid numbers that should fail the Luhn Algorithm check.
        """
        invalid_numbers = [
            "4532015112830365",  # Invalid credit card number
            "6011111111111118",  # Invalid credit card number
            "79927398710",  # Invalid number
        ]
        for number in invalid_numbers:
            luhn = LuhnAlgorithm(number)
            self.assertFalse(luhn.is_valid(), f"Number {number} should be invalid.")

    def test_non_digit_characters(self):
        """
        Test numbers with non-digit characters (e.g., spaces, hyphens).
        The algorithm should ignore non-digit characters.
        """
        numbers_with_non_digits = [
            "4532 0151 1283 0366",  # Valid number with spaces
            "6011-1111-1111-1117",  # Valid number with hyphens
            "7992-7398-713",  # Valid number with hyphens
        ]
        for number in numbers_with_non_digits:
            luhn = LuhnAlgorithm(number)
            self.assertTrue(
                luhn.is_valid(), f"Number {number} should be valid after cleaning."
            )

    def test_empty_input(self):
        """
        Test empty input. The algorithm should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            luhn = LuhnAlgorithm("")
            luhn.is_valid()

    def test_input_with_no_digits(self):
        """
        Test input with no digits (e.g., only special characters).
        The algorithm should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            luhn = LuhnAlgorithm("!@#$%^&*()")
            luhn.is_valid()

    def test_single_digit_input(self):
        """
        Test input with a single digit. The algorithm should handle it correctly.
        """
        luhn = LuhnAlgorithm("0")
        self.assertTrue(luhn.is_valid(), "Single digit '0' should be valid.")

    def test_large_valid_number(self):
        """
        Test a large valid number to ensure the algorithm handles long inputs.
        """
        large_valid_number = "1234567812345670"  # Valid number
        luhn = LuhnAlgorithm(large_valid_number)
        self.assertTrue(
            luhn.is_valid(), f"Number {large_valid_number} should be valid."
        )

    def test_large_invalid_number(self):
        """
        Test a large invalid number to ensure the algorithm handles long inputs.
        """
        large_invalid_number = "1234567812345678"  # Invalid number
        luhn = LuhnAlgorithm(large_invalid_number)
        self.assertFalse(
            luhn.is_valid(), f"Number {large_invalid_number} should be invalid."
        )


if __name__ == "__main__":
    unittest.main()
