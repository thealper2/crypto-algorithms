from typing import Callable


class HMAC:
    """
    HMAC (Hash-based Message Authentication Code) implementation in Python.
    """

    def __init__(
        self,
        key: bytes,
        message: bytes,
        hash_func: Callable[[bytes], bytes],
        block_size: int = 64,
    ):
        """
        Initialize the HMAC class.

        Args:
            key (bytes): The secret key for HMAC.
            message (bytes): The message to authenticate.
            hash_func (Callable[[bytes], bytes]): A custom hash functoin that takes bytes and returns a hash as bytes.
            block_size (int): The block size of the hash function. Default is 64 bytes for SHA-256.
        """
        self.key = key
        self.message = message
        self.hash_func = hash_func
        self.block_size = block_size

        # Ensure the key is of block_size length
        if len(self.key) > self.block_size:
            self.key = self.hash_func(self.key)
        elif len(self.key) < self.block_size:
            self.key = self.key.ljust(self.block_size, b"\x00")

    def _xor_bytes(self, a: bytes, b: bytes) -> bytes:
        """
        XOR operation between two byte strings.

        Args:
            a (bytes): First byte string.
            b (bytes): Second byte string.

        Returns:
            bytes: Resulting byte string after XOR operation.
        """
        return bytes(x ^ y for x, y in zip(a, b))

    def generate(self) -> bytes:
        """
        Generate the HMAC for the given key and message.

        Returns:
            bytes: The HMAC as a byte string.
        """
        try:
            # Create the inner and outer padding
            ipad = b"\x36" * self.block_size
            opad = b"\x5c" * self.block_size

            # XOR the key with the padding values
            i_key_pad = self._xor_bytes(self.key, ipad)
            o_key_pad = self._xor_bytes(self.key, opad)

            # Perform the inner hash
            inner_hash = self.hash_func(i_key_pad + self.message)

            # Perform the outer hash
            hmac = self.hash_func(o_key_pad + inner_hash)
            return hmac

        except Exception as e:
            raise RuntimeError(f"Error generating HMAC: {e}")
