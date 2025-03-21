from typing import List


class MD5:
    """
    A class to compute the MD5 hash of a given input message.
    """

    def __init__(self):
        # Initialize MD5 buffer with magic constants
        self.A = 0x67452301
        self.B = 0xEFCDAB89
        self.C = 0x98BADCFE
        self.D = 0x10325476

        # Define shift amounts for each round
        self.shift_amounts: List[int] = [
            7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
            5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
            4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
            6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
        ]
        
        # Define sine function constants
        self.T: List[int] = [
            int(abs(__import__("math").sin(i + 1)) * 2**32) & 0xFFFFFFFF
            for i in range(64)
        ]

    @staticmethod
    def left_rotate(x: int, n: int) -> int:
        """
        Perform a left rotation (circular shift) on a 32-bit integer.

        Args:
            x (int): The integer to rotate.
            n (int): The number of bits to rotate.

        Returns:
            int: The rotated integer.
        """
        return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF

    def _pad_message(self, message: bytes) -> bytes:
        """
        Pad the message to ensure its length is congruent to 448 modulo 512.

        Args:
            message (bytes): The input message as bytes.

        Returns:
            bytes: The padded message as bytes.
        """
        original_length = len(message) * 8  # Length in bits
        message += b"\x80"  # Append a single '1' bit

        # Append '0' bits until the length is 448 mod 512
        while (len(message) * 8 + 64) % 512 != 0:
            message += b"\x00"

        # Append the original length in bits at the end (little-endian)
        message += original_length.to_bytes(8, byteorder="little")
        return message

    def _process_chunk(self, chunk: bytes) -> None:
        """
        Process a 512-bit chunk of the message.

        Args:
            chunk (bytes): A 512-bit chunk of the message.
        """
        # Break the chunk into 16 words (32 bits each)
        words = [
            int.from_bytes(chunk[i : i + 4], byteorder="little")
            for i in range(0, 64, 4)
        ]

        # Initialize hash values for this chunk
        a, b, c, d = self.A, self.B, self.C, self.D

        # Main MD5 compression function
        for i in range(64):
            if 0 <= i <= 15:
                f = (b & c) | (~b & d)
                g = i
            elif 16 <= i <= 31:
                f = (d & b) | (~d & c)
                g = (5 * i + 1) % 16
            elif 32 <= i <= 47:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7 * i) % 16

            f = (f + a + self.T[i] + words[g]) & 0xFFFFFFFF
            a, d, c, b = (
                d,
                c,
                b,
                (b + self.left_rotate(f, self.shift_amounts[i])) & 0xFFFFFFFF,
            )

        # Update the hash values
        self.A = (self.A + a) & 0xFFFFFFFF
        self.B = (self.B + b) & 0xFFFFFFFF
        self.C = (self.C + c) & 0xFFFFFFFF
        self.D = (self.D + d) & 0xFFFFFFFF

    def compute_md5(self, message: str) -> str:
        """
        Compute the MD5 hash of the input message.

        Args:
            message (str): The input message as a string.

        Returns:
            str: The MD5 hash as a 32-character hexadecimal string.
        """
        try:
            # Convert the message to bytes
            message_bytes = message.encode("utf-8")

            # Pad the message
            padded_message = self._pad_message(message_bytes)

            # Process the message in 512-bit chunks
            for i in range(0, len(padded_message), 64):
                chunk = padded_message[i : i + 64]
                self._process_chunk(chunk)

            # Produce the final hash value
            hash_value = (
                self.A.to_bytes(4, byteorder="little")
                + self.B.to_bytes(4, byteorder="little")
                + self.C.to_bytes(4, byteorder="little")
                + self.D.to_bytes(4, byteorder="little")
            )

            return hash_value.hex()
        except Exception as e:
            raise RuntimeError(f"Error computing MD5 hash: {e}")
