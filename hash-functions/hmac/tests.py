import unittest
from hmac import HMAC
from utils import custom_hash_function


class TestHMAC(unittest.TestCase):
    """
    Test cases for the HMAC implementation.
    """

    def test_hmac_generation(self):
        """
        Test HMAC generation with a simple key and message.
        """
        key = b"secret_key"
        message = b"hello_world"
        hmac_generator = HMAC(key, message, custom_hash_function)
        hmac = hmac_generator.generate()

        # Since we're using a custom hash function, we can predict the output
        # For the dummy hash function: custom_hash_function(byte) = byte ^ 0xFF
        # So, we can manually compute the expected HMAC
        expected_hmac = custom_hash_function(
            bytes(
                [x ^ 0x5C for x in key.ljust(64, b"\x00")]
                + custom_hash_function(
                    bytes([x ^ 0x36 for x in key.ljust(64, b"\x00")] + message)
                )
            )
        )
        self.assertEqual(hmac, expected_hmac)

    def test_key_longer_than_block_size(self):
        """
        Test HMAC generation when the key is longer than the block size.
        The key should be hashed to fit the block size.
        """
        key = b"a_very_long_key_that_is_longer_than_the_block_size_of_64_bytes"
        message = b"test_message"
        hmac_generator = HMAC(key, message, custom_hash_function)
        hmac = hmac_generator.generate()

        # Ensure the key is hashed to fit the block size
        hashed_key = custom_hash_function(key)
        expected_hmac = custom_hash_function(
            bytes([x ^ 0x5C for x in hashed_key.ljust(64, b"\x00")])
            + custom_hash_function(
                bytes([x ^ 0x36 for x in hashed_key.ljust(64, b"\x00")] + message)
            )
        )
        self.assertEqual(hmac, expected_hmac)

    def test_key_shorter_than_block_size(self):
        """
        Test HMAC generation when the key is shorter than the block size.
        The key should be padded with zeros to fit the block size.
        """
        key = b"short_key"
        message = b"test_message"
        hmac_generator = HMAC(key, message, custom_hash_function)
        hmac = hmac_generator.generate()

        # Ensure the key is padded with zeros
        padded_key = key.ljust(64, b"\x00")
        expected_hmac = custom_hash_function(
            bytes(
                [x ^ 0x5C for x in padded_key]
                + custom_hash_function(bytes([x ^ 0x36 for x in padded_key] + message))
            )
        )
        self.assertEqual(hmac, expected_hmac)

    def test_empty_message(self):
        """
        Test HMAC generation with an empty message.
        """
        key = b"secret_key"
        message = b""
        hmac_generator = HMAC(key, message, custom_hash_function)
        hmac = hmac_generator.generate()

        # Compute the expected HMAC for an empty message
        expected_hmac = custom_hash_function(
            bytes([x ^ 0x5C for x in key.ljust(64, b"\x00")])
            + custom_hash_function(
                bytes([x ^ 0x36 for x in key.ljust(64, b"\x00")] + message)
            )
        )
        self.assertEqual(hmac, expected_hmac)

    def test_empty_key(self):
        """
        Test HMAC generation with an empty key.
        """
        key = b""
        message = b"test_message"
        hmac_generator = HMAC(key, message, custom_hash_function)
        hmac = hmac_generator.generate()

        # Compute the expected HMAC for an empty key
        padded_key = key.ljust(64, b"\x00")
        expected_hmac = custom_hash_function(
            bytes([x ^ 0x5C for x in padded_key])
            + custom_hash_function(bytes([x ^ 0x36 for x in padded_key] + message))
        )
        self.assertEqual(hmac, expected_hmac)

    def test_invalid_hash_function(self):
        """
        Test HMAC generation with an invalid hash function.
        The hash function must accept bytes and return bytes.
        """
        key = b"secret_key"
        message = b"test_message"

        # Define an invalid hash function that returns a string instead of bytes
        def invalid_hash_function(data: bytes) -> str:
            return "invalid_hash"

        with self.assertRaises(RuntimeError):
            hmac_generator = HMAC(key, message, invalid_hash_function)
            hmac_generator.generate()


if __name__ == "__main__":
    unittest.main()
