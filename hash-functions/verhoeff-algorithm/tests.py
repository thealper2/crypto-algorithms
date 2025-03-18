import unittest
from verhoeff import VerhoeffAlgorithm


class TestVerhoeffAlgorithm(unittest.TestCase):
    """
    A test class for the VerhoeffAlgorithm implementation.
    """

    def setUp(self) -> None:
        """
        Set up the test environment by creating an instance of VerhoeffAlgorithm.
        """
        self.verhoeff = VerhoeffAlgorithm()

    def test_compute_checksum_valid_input(self) -> None:
        """
        Test the compute_checksum method with valid input.
        """
        # Test case 1: Valid number
        self.assertEqual(self.verhoeff.compute_checksum("12345"), 1)
        # Test case 2: Valid number with leading zeros
        self.assertEqual(self.verhoeff.compute_checksum("0012345"), 1)
        # Test case 3: Single-digit number
        self.assertEqual(self.verhoeff.compute_checksum("5"), 8)

    def test_compute_checksum_invalid_input(self) -> None:
        """
        Test the compute_checksum method with invalid input.
        """
        # Test case 1: Non-numeric input
        with self.assertRaises(ValueError):
            self.verhoeff.compute_checksum("12A45")
        # Test case 2: Empty string
        with self.assertRaises(ValueError):
            self.verhoeff.compute_checksum("")

    def test_validate_number_valid_input(self) -> None:
        """
        Test the validate_number method with valid input.
        """
        # Test case 1: Valid number with correct checksum
        self.assertTrue(self.verhoeff.validate_number("123451"))
        # Test case 2: Valid number with incorrect checksum
        self.assertFalse(self.verhoeff.validate_number("12345"))
        # Test case 3: Valid number with leading zeros
        self.assertTrue(self.verhoeff.validate_number("00123451"))

    def test_validate_number_invalid_input(self) -> None:
        """
        Test the validate_number method with invalid input.
        """
        # Test case 1: Non-numeric input
        with self.assertRaises(ValueError):
            self.verhoeff.validate_number("12A45")
        # Test case 2: Empty string
        with self.assertRaises(ValueError):
            self.verhoeff.validate_number("")

    def test_edge_cases(self) -> None:
        """
        Test edge cases for both compute_checksum and validate_number methods.
        """
        # Test case 1: Large number
        self.assertEqual(self.verhoeff.compute_checksum("987654321"), 7)
        self.assertTrue(self.verhoeff.validate_number("9876543217"))
        # Test case 2: All zeros
        self.assertEqual(self.verhoeff.compute_checksum("0000"), 0)
        self.assertTrue(self.verhoeff.validate_number("00000"))


if __name__ == "__main__":
    unittest.main()
