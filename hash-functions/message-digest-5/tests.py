import unittest
from md5 import MD5


class TestMD5(unittest.TestCase):
    """
    Test suite for the MD5 class implementation.
    """

    def test_empty_string(self):
        """
        Test MD5 hash of an empty string.
        Expected output: d41d8cd98f00b204e9800998ecf8427e
        """
        md5 = MD5()
        result = md5.compute_md5("")
        self.assertEqual(result, "d41d8cd98f00b204e9800998ecf8427e")

    def test_single_character(self):
        """
        Test MD5 hash of a single character.
        Expected output: 0cc175b9c0f1b6a831c399e269772661
        """
        md5 = MD5()
        result = md5.compute_md5("a")
        self.assertEqual(result, "0cc175b9c0f1b6a831c399e269772661")

    def test_common_string(self):
        """
        Test MD5 hash of a common string.
        Expected output: 900150983cd24fb0d6963f7d28e17f72
        """
        md5 = MD5()
        result = md5.compute_md5("abc")
        self.assertEqual(result, "900150983cd24fb0d6963f7d28e17f72")

    def test_long_string(self):
        """
        Test MD5 hash of a longer string.
        Expected output: 9e107d9d372bb6826bd81d3542a419d6
        """
        md5 = MD5()
        result = md5.compute_md5("The quick brown fox jumps over the lazy dog")
        self.assertEqual(result, "9e107d9d372bb6826bd81d3542a419d6")

    def test_string_with_special_characters(self):
        """
        Test MD5 hash of a string containing special characters.
        Expected output: 6cd3556deb0da54bca060b4c39479839
        """
        md5 = MD5()
        result = md5.compute_md5("Hello, world!")
        self.assertEqual(result, "6cd3556deb0da54bca060b4c39479839")

    def test_large_input(self):
        """
        Test MD5 hash of a large input string.
        Expected output: cabe45dcc9ae5b66ba86600cca6b8ba8
        """
        md5 = MD5()
        large_input = "a" * 1000  # 1000 times the character 'a'
        result = md5.compute_md5(large_input)
        self.assertEqual(result, "cabe45dcc9ae5b66ba86600cca6b8ba8")

    def test_non_ascii_input(self):
        """
        Test MD5 hash of a string containing non-ASCII characters.
        Expected output: c0e89a293bd36c7a768e4e9d2c5475a8
        """
        md5 = MD5()
        result = md5.compute_md5("こんにちは")  # Japanese greeting
        self.assertEqual(result, "c0e89a293bd36c7a768e4e9d2c5475a8")


if __name__ == "__main__":
    unittest.main()
