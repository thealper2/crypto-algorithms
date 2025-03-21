import struct


class MD4:
    """
    A Python implementation of the MD4 hashing algorithm.

    Attributes:
        A, B, C, D (int): Initial buffer values for MD4.
        shift (list): List of shift amounts for each round.
    """

    def __init__(self):
        """
        Initialize the MD4 class with initial buffer values and shift amounts.
        """
        self.A = 0x67452301
        self.B = 0xEFCDAB89
        self.C = 0x98BADCFE
        self.D = 0x10325476
        self.shift = [3, 7, 11, 19, 3, 5, 9, 13, 3, 9, 11, 15]

    @staticmethod
    def left_rotate(value: int, shift: int) -> int:
        """
        Perform a left rotation (circular shift) on a 32-bit integer.

        Args:
            value (int): The value to rotate.
            shift (int): The number of bits to rotate.

        Returns:
            int: The rotated value.
        """
        return ((value << shift) & 0xFFFFFFFF) | (value >> (32 - shift))

    def _f(self, x: int, y: int, z: int) -> int:
        """
        MD4 F function: (x & y) | (~x & z).
        """
        return (x & y) | (~x & z)

    def _g(self, x: int, y: int, z: int) -> int:
        """
        MD4 G function: (x & y) | (x & z) | (y & z).
        """
        return (x & y) | (x & z) | (y & z)

    def _h(self, x: int, y: int, z: int) -> int:
        """
        MD4 H function: x ^ y ^ z.
        """
        return x ^ y ^ z

    def _process_block(self, block: bytes) -> None:
        """
        Process a 64-byte block of data.

        Args:
            block (bytes): The 64-byte block to process.
        """
        # Unpack the block into 16 32-bit words
        X = list(struct.unpack("<16I", block))

        # Save the current state
        AA, BB, CC, DD = self.A, self.B, self.C, self.D

        # Round I
        for i in range(16):
            k = i
            s = self.shift[i % 4]
            self.A = self.left_rotate(
                (self.A + self._f(self.B, self.C, self.D) + X[k]) & 0xFFFFFFFF, s
            )

            # Rotate the buffers
            self.A, self.B, self.C, self.D = self.D, self.A, self.B, self.C

        # Round 2
        for i in range(16):
            k = (i % 4) * 4 + (i // 4)
            s = self.shift[4 + (i % 4)]
            self.A = self.left_rotate(
                (self.A + self._g(self.B, self.C, self.D) + X[k] + 0x5A827999)
                & 0xFFFFFFFF,
                s,
            )

            # Rotate the buffers
            self.A, self.B, self.C, self.D = self.D, self.A, self.B, self.C

        # Round 3
        for i in range(16):
            k = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15][i]
            s = self.shift[8 + (i % 4)]
            self.A = self.left_rotate(
                (self.A + self._h(self.B, self.C, self.D) + X[k] + 0x6ED9EBA1)
                & 0xFFFFFFFF,
                s,
            )

            # Rotate the buffers
            self.A, self.B, self.C, self.D = self.D, self.A, self.B, self.C

        # Update the state
        self.A = (self.A + AA) & 0xFFFFFFFF
        self.B = (self.B + BB) & 0xFFFFFFFF
        self.C = (self.C + CC) & 0xFFFFFFFF
        self.D = (self.D + DD) & 0xFFFFFFFF

    def hash(self, message: bytes) -> bytes:
        """
        Compute the MD4 hash of a message.

        Args:
            message (bytes): The message to hash.

        Returns:
            bytes: The 16-byte MD4 hash of the message.
        """
        # Pad the message
        original_length = len(message)
        message += b"\x80"
        message += b"\x00" * ((56 - (original_length + 1) % 64) % 64)
        message += struct.pack("<Q", original_length * 8)

        # Process each 64-byte block
        for i in range(0, len(message), 64):
            self._process_block(message[i : i + 64])

        # Pack the final state into a 16-byte hash
        return struct.pack("<4I", self.A, self.B, self.C, self.D)
