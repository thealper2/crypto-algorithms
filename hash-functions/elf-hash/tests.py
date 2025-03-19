import unittest
from elf import ElfHash


class TestElfHash(unittest.TestCase):
    """
    Test suite for the ElfHash class.
    """

    def test_compute_hash_valid_input(self):
        """
        Test the compute_hash method with a valid input string.
        """
        elf_hash = ElfHash()
        result = elf_hash.compute_hash("hello")
        self.assertEqual(result, 7258927)  # Expected hash value for "hello"

    def test_compute_hash_empty_string(self):
        """
        Test the compute_hash method with an empty string.
        This should raise a ValueError.
        """
        elf_hash = ElfHash()
        with self.assertRaises(ValueError):
            elf_hash.compute_hash("")

    def test_compute_hash_special_characters(self):
        """
        Test the compute_hash method with a string containing special characters.
        """
        elf_hash = ElfHash()
        result = elf_hash.compute_hash("!@#$%^&*()")
        self.assertEqual(result, 112385785)  # Expected hash value for "!@#$%^&*()"

    def test_compute_hash_long_string(self):
        """
        Test the compute_hash method with a long string.
        """
        elf_hash = ElfHash()
        long_string = "a" * 1000  # A string with 1000 'a' characters
        result = elf_hash.compute_hash(long_string)
        self.assertEqual(
            result, 423793
        )  # Expected hash value for a long string of 'a's

    def test_get_hash_before_computation(self):
        """
        Test the get_hash method before any hash computation.
        This should return None.
        """
        elf_hash = ElfHash()
        self.assertIsNone(elf_hash.get_hash())

    def test_get_hash_after_computation(self):
        """
        Test the get_hash method after computing a hash.
        """
        elf_hash = ElfHash()
        elf_hash.compute_hash("test")
        self.assertEqual(elf_hash.get_hash(), 502948)  # Expected hash value for "test"

    def test_compute_hash_case_sensitivity(self):
        """
        Test the compute_hash method with case-sensitive input.
        """
        elf_hash = ElfHash()
        result_lower = elf_hash.compute_hash("hello")
        result_upper = elf_hash.compute_hash("HELLO")
        self.assertNotEqual(
            result_lower, result_upper
        )  # Hash values should differ for different cases

    def test_compute_hash_whitespace(self):
        """
        Test the compute_hash method with a string containing whitespace.
        """
        elf_hash = ElfHash()
        result = elf_hash.compute_hash("hello world")
        self.assertEqual(result, 18131988)  # Expected hash value for "hello world"

    def test_compute_hash_numbers(self):
        """
        Test the compute_hash method with a string containing numbers.
        """
        elf_hash = ElfHash()
        result = elf_hash.compute_hash("12345")
        self.assertEqual(result, 3430005)  # Expected hash value for "12345"

    def test_compute_hash_mixed_characters(self):
        """
        Test the compute_hash method with a string containing mixed characters.
        """
        elf_hash = ElfHash()
        result = elf_hash.compute_hash("h3ll0 W0rld!")
        self.assertEqual(result, 52280641)  # Expected hash value for "h3ll0 W0rld!"


if __name__ == "__main__":
    unittest.main()
