import unittest
from djb2 import DJB2Hash


class TestDJB2Hash(unittest.TestCase):
    """
    Test suite for the DJB2Hash class.
    """

    def test_hash_empty_string(self):
        """
        Test hashing an empty string.
        The hash value should remain the initial value (5381).
        """
        djb2 = DJB2Hash()
        djb2.update("")
        self.assertEqual(djb2.digest(), 5381, "Hash of an empty string should be 5381.")

    def test_hash_single_character(self):
        """
        Test hashing a single character.
        The hash value should be computed correctly based on the DJB2 algorithm.
        """
        djb2 = DJB2Hash()
        djb2.update("a")
        # Expected hash: ((5381 << 5) + 5381) + ord('a') = 177670
        self.assertEqual(djb2.digest(), 177670, "Hash of 'a' should be 177670.")

    def test_hash_multiple_characters(self):
        """
        Test hashing a string with multiple characters.
        The hash value should be computed correctly based on the DJB2 algorithm.
        """
        djb2 = DJB2Hash()
        djb2.update("hello")
        # Expected hash: computed step-by-step using the DJB2 algorithm
        expected_hash = 210714636441
        self.assertEqual(
            djb2.digest(), expected_hash, "Hash of 'hello' should be 210714636441."
        )

    def test_hash_non_string_input(self):
        """
        Test passing a non-string input to the update method.
        A TypeError should be raised.
        """
        djb2 = DJB2Hash()
        with self.assertRaises(
            TypeError, msg="Updating with a non-string input should raise a TypeError."
        ):
            djb2.update(123)  # Passing an integer, which is invalid

    def test_hexdigest(self):
        """
        Test the hexdigest method to ensure it returns the correct hexadecimal representation.
        """
        djb2 = DJB2Hash()
        djb2.update("hello")
        # Expected hex digest of the hash for "hello"
        expected_hex = "0x310f923099"
        self.assertEqual(
            djb2.hexdigest(),
            expected_hex,
            "Hex digest of 'hello' should be 0x310f923099.",
        )

    def test_large_input(self):
        """
        Test hashing a large input string.
        The hash value should be computed correctly without errors.
        """
        djb2 = DJB2Hash()
        large_input = "a" * 100000  # A string with 100,000 'a' characters
        djb2.update(large_input)
        # Ensure no errors occur and the hash is computed
        self.assertIsInstance(
            djb2.digest(), int, "Hashing a large input should return an integer."
        )


if __name__ == "__main__":
    unittest.main()
