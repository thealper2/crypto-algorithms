from typing import Union


class MurmurHash:
    """
    A Python implementation of a the MurmurHash algorithm.

    Attributes:
        seed (int): A seed value for the hash function. Default is 0.
    """

    def __init__(self, seed: int = 0):
        """
        Initializes the MurmurHash object with an optional seed.

        Args:
            seed (int): A seed value for the hash function. Default is 0.
        """
        self.seed = seed

    def hash(self, key: Union[str, bytes]) -> int:
        """
        Computes the MurmurHash3 hash of the input key.

        Args:
            key (Union[str, bytes]): The input key to hash. Can be a string or bytes.

        Returns:
            int: The 32-bit hash value of the input key.

        Raises:
            TypeError: If the input key is not a string or bytes.
        """
        if isinstance(key, str):
            key = key.encode("utf-8")  # Convert string or bytes
        elif not isinstance(key, bytes):
            raise TypeError("Input key must be a string or bytes.")

        length = len(key)
        h = self.seed
        c1 = 0xCC9E2D51
        c2 = 0x1B873593

        # Process the key in 4-byte chunks
        for i in range(0, length - (length % 4), 4):
            k = key[i] | (key[i + 1] << 8) | (key[i + 2] << 16) | (key[i + 3] << 24)
            k = (k * c1) & 0xFFFFFFFF
            k = ((k << 15) | (k >> 17)) & 0xFFFFFFFF  # Rotate left by 15 bits
            k = (k * c2) & 0xFFFFFFFF
            h ^= k
            h = ((h << 13) | (h >> 19)) & 0xFFFFFFFF  # Rotate left by 13 bits
            h = (h * 5 + 0xE6546B64) & 0xFFFFFFFF

        # Process remaining bytes
        remaining = length % 4
        if remaining:
            k = 0
            for i in range(remaining):
                k |= key[length - remaining + i] << (8 * i)

            k = (k * c1) & 0xFFFFFFFF
            k = ((k << 15) | (k >> 17)) & 0xFFFFFFFF
            k = (k * c2) & 0xFFFFFFFF
            h ^= k

        # Finalize the hash
        h ^= length
        h ^= h >> 16
        h = (h * 0x85EBCA6B) & 0xFFFFFFFF
        h ^= h >> 13
        h = (h * 0xC2B2AE35) & 0xFFFFFFFF
        h ^= h >> 16
        return h
