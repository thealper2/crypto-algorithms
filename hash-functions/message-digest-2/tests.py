import unittest
from md2 import MD2


class TestMD2(unittest.TestCase):
    """
    Test cases for the MD2 hashing algorithm implementation.
    """

    def test_empty_string(self):
        """
        Test MD2 hash of an empty string.
        The expected hash is known for an empty input.
        """
        md2 = MD2()
        self.assertEqual(md2.hash(b""), "8350e5a3e24c153df2275c9f80692773")

    def test_short_message(self):
        """
        Test MD2 hash of a short message.
        The expected hash is known for the input "Hello, World!".
        """
        md2 = MD2()
        self.assertEqual(md2.hash(b"Hello, World!"), "1c8f1e6a94aaa7145210bf90bb52871a")

    def test_long_message(self):
        """
        Test MD2 hash of a long message.
        The expected hash is known for a specific long input.
        """
        md2 = MD2()
        long_message = b"a" * 1000  # 1000 times 'a'
        self.assertEqual(md2.hash(long_message), "dd21a412ef3f285fd1f2e70a6c10a702")

    def test_non_ascii_message(self):
        """
        Test MD2 hash of a message containing non-ASCII characters.
        """
        md2 = MD2()
        non_ascii_message = "こんにちは".encode("utf-8")  # Japanese greeting
        self.assertEqual(
            md2.hash(non_ascii_message), "506f145fafb008a4f6746b4604083ba2"
        )

    def test_invalid_input_type(self):
        """
        Test that the hash method raises a TypeError for invalid input types.
        """
        md2 = MD2()
        with self.assertRaises(TypeError):
            md2.hash("This is not bytes")  # Input is a string, not bytes

    def test_known_hash_value(self):
        """
        Test MD2 hash against a known hash value for a specific input.
        """
        md2 = MD2()
        known_input = b"The quick brown fox jumps over the lazy dog"
        known_hash = "03d85a0d629d2c442e987525319fc471"
        self.assertEqual(md2.hash(known_input), known_hash)

    def test_padding(self):
        """
        Test that the padding function works correctly.
        The input length is not a multiple of 16, so padding should be added.
        """
        md2 = MD2()
        input_message = b"123456789012345"  # 15 bytes
        padded_message = md2._pad_message(input_message)
        self.assertEqual(len(padded_message), 16)  # Padded to 16 bytes
        self.assertEqual(padded_message[-1], 1)  # Last byte should be 1

    def test_checksum_update(self):
        """
        Test that the checksum is updated correctly for a given block.
        """
        md2 = MD2()
        block = [0x61] * 16  # Block of 16 'a' characters
        md2._update_checksum(block)
        # Manually compute the expected checksum
        expected_checksum = [0x61 ^ md2.S[0x61 ^ 0]] * 16
        self.assertEqual(md2.checksum, expected_checksum)

    def test_process_block(self):
        """
        Test that the state is updated correctly after processing a block.
        """
        md2 = MD2()
        block = [0x61] * 16  # Block of 16 'a' characters
        md2._process_block(block)
        # The state should be updated after processing the block
        self.assertNotEqual(md2.state, [0] * 48)


if __name__ == "__main__":
    unittest.main()
