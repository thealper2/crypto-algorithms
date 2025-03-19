import unittest
from damm import DammAlgorithm


class TestDammAlgorithm(unittest.TestCase):
    """
    A test class for the DammAlgorithm implementation.
    """

    def setUp(self) -> None:
        """
        Set up the DammAlgorithm instance for testing.
        """
        self.damm = DammAlgorithm()

    def test_compute_check_digit(self) -> None:
        """
        Test the compute_check_digit method with valid inputs.
        """
        # Test cases with known results
        self.assertEqual(
            self.damm.compute_check_digit(572), 4, "Check digit for 572 should be 4"
        )
        self.assertEqual(
            self.damm.compute_check_digit(12345), 1, "Check digit for 12345 should be 1"
        )
        self.assertEqual(
            self.damm.compute_check_digit(0), 0, "Check digit for 0 should be 0"
        )

    def test_compute_check_digit_negative_input(self) -> None:
        """
        Test the compute_check_digit method with negative input.
        """
        with self.assertRaises(
            ValueError, msg="Negative input should raise ValueError"
        ):
            self.damm.compute_check_digit(-123)

    def test_validate_number_valid(self) -> None:
        """
        Test the validate_number method with valid numbers.
        """
        # Valid numbers with correct check digits
        self.assertTrue(self.damm.validate_number(5724), "5724 should be valid")
        self.assertTrue(self.damm.validate_number(123451), "123451 should be valid")
        self.assertTrue(self.damm.validate_number(00), "00 should be valid")

    def test_validate_number_invalid(self) -> None:
        """
        Test the validate_number method with invalid numbers.
        """
        # Invalid numbers with incorrect check digits
        self.assertFalse(self.damm.validate_number(5723), "5723 should be invalid")
        self.assertFalse(self.damm.validate_number(123450), "123450 should be invalid")

    def test_validate_number_negative_input(self) -> None:
        """
        Test the validate_number method with negative input.
        """
        with self.assertRaises(
            ValueError, msg="Negative input should raise ValueError"
        ):
            self.damm.validate_number(-1234)


if __name__ == "__main__":
    unittest.main()
