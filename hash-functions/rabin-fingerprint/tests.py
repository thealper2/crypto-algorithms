import unittest
from rabin import RabinFingerprint


class TestRabinFingerprint(unittest.TestCase):
    """
    A test class for the RabinFingerprint implementation.
    """

    def setUp(self):
        """
        Set up the RabinFingerprint instance with default base and modulus for testing.
        """
        self.rabin = RabinFingerprint(base=256, modulus=101)

    def test_compute_empty_string(self):
        """
        Test the compute method with an empty string.
        Expected result: None
        """
        result = self.rabin.compute("")
        self.assertIsNone(result, "Empty string should return None")

    def test_compute_single_character(self):
        """
        Test the compute method with a single character.
        Expected result: The ASCII value of the character modulo the modulus.
        """
        result = self.rabin.compute("a")
        expected = ord("a") % 101
        self.assertEqual(result, expected, "Single character fingerprint is incorrect")

    def test_compute_multiple_characters(self):
        """
        Test the compute method with a string of multiple characters.
        Expected result: The computed fingerprint using the polynomial rolling hash.
        """
        result = self.rabin.compute("hello")
        # Manually compute the expected fingerprint
        expected = (
            ord("h") * 256**4
            + ord("e") * 256**3
            + ord("l") * 256**2
            + ord("l") * 256
            + ord("o")
        ) % 101
        self.assertEqual(
            result, expected, "Multiple characters fingerprint is incorrect"
        )

    def test_rolling_hash_valid_input(self):
        """
        Test the rolling_hash method with valid input.
        Expected result: The updated rolling hash after removing the old character and adding the new character.
        """
        # Compute the initial fingerprint for "hello"
        initial_fingerprint = self.rabin.compute("hello")
        # Compute the rolling hash for removing 'h' and adding 'a'
        result = self.rabin.rolling_hash("h", "a", initial_fingerprint)
        # Manually compute the expected rolling hash
        expected = ((initial_fingerprint - ord("h") * (256**4)) * 256 + ord("a")) % 101
        self.assertEqual(result, expected, "Rolling hash computation is incorrect")

    def test_rolling_hash_invalid_input(self):
        """
        Test the rolling_hash method with invalid input (empty strings).
        Expected result: None
        """
        result = self.rabin.rolling_hash("", "", 123)
        self.assertIsNone(result, "Invalid input should return None")

    def test_compute_non_ascii_characters(self):
        """
        Test the compute method with non-ASCII characters.
        Expected result: The computed fingerprint using the polynomial rolling hash.
        """
        result = self.rabin.compute("çáé")
        # Manually compute the expected fingerprint
        expected = (ord("ç") * 256**2 + ord("á") * 256 + ord("é")) % 101
        self.assertEqual(
            result, expected, "Non-ASCII characters fingerprint is incorrect"
        )

    def test_compute_large_input(self):
        """
        Test the compute method with a large input string.
        Expected result: The computed fingerprint using the polynomial rolling hash.
        """
        large_input = "a" * 1000  # A string with 1000 'a' characters
        result = self.rabin.compute(large_input)
        # Manually compute the expected fingerprint
        expected = (ord("a") * (256**999 + 256**998 + ... + 256 + 1)) % 101
        # Simplify the computation using the geometric series formula
        expected = (ord("a") * (256**1000 - 1) // (256 - 1)) % 101
        self.assertEqual(result, expected, "Large input fingerprint is incorrect")


if __name__ == "__main__":
    unittest.main()
