import unittest
from adler32 import Adler32


class TestAdler32(unittest.TestCase):
    """
    A test suite for the Adler32 class.
    """

    def test_empty_input(self):
        """
        Test the Adler-32 checksum computation for an empty input.
        """
        adler32 = Adler32()
        adler32.update(b"")
        self.assertEqual(
            adler32.digest(), 0x00000001, "Empty input should return 0x00000001"
        )

    def test_single_byte_input(self):
        """
        Test the Adler-32 checksum computation for a single byte input.
        """
        adler32 = Adler32()
        adler32.update(b"a")
        self.assertEqual(
            adler32.digest(), 0x00620062, "Checksum for 'a' should be 0x00620062"
        )

    def test_multibyte_input(self):
        """
        Test the Adler-32 checksum computation for a multi-byte input.
        """
        adler32 = Adler32()
        adler32.update(b"Hello, World!")
        self.assertEqual(
            adler32.digest(),
            0x1F9E046A,
            "Checksum for 'Hello, World!' should be 0x1F9E046A",
        )

    def test_large_input(self):
        """
        Test the Adler-32 checksum computation for a large input.
        """
        adler32 = Adler32()
        data = b"a" * 1000  # 1000 bytes of 'a'
        adler32.update(data)
        self.assertEqual(
            adler32.digest(), 0xF9D87AF8, "Checksum for 1000 'a's should be 0xF9D87AF8"
        )

    def test_reset_functionality(self):
        """
        Test the reset functionality of the Adler32 class.
        """
        adler32 = Adler32()
        adler32.update(b"Hello")
        adler32.reset()
        adler32.update(b"World")
        self.assertEqual(
            adler32.digest(),
            0x06060209,
            "Checksum for 'World' should be 0x06060209 after reset",
        )

    def test_hexdigest_functionality(self):
        """
        Test the hexdigest functionality of the Adler32 class.
        """
        adler32 = Adler32()
        adler32.update(b"Hello, World!")
        self.assertEqual(
            adler32.hexdigest(),
            "1F9E046A",
            "Hex checksum for 'Hello, World!' should be '1F9E046A'",
        )

    def test_invalid_input_type(self):
        """
        Test that a TypeError is raised when the input is not of type bytes or bytearray.
        """
        adler32 = Adler32()
        with self.assertRaises(TypeError):
            adler32.update("This is not bytes")  # Passing a string instead of bytes

    def test_multiple_updates(self):
        """
        Test the Adler-32 checksum computation when the input is provided in multiple updates.
        """
        adler32 = Adler32()
        adler32.update(b"Hello, ")
        adler32.update(b"World!")
        self.assertEqual(
            adler32.digest(),
            0x1F9E046A,
            "Checksum for 'Hello, World!' should be 0x1F9E046A even with multiple updates",
        )


if __name__ == "__main__":
    unittest.main()
