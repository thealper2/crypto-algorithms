from typing import List


class SHA256:
    """
    A class to implement the SHA-256 hashing algorithm.
    """

    # Constants for SHA-256
    K: List[int] = [
        0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
    ]
    
    def __init__(self) -> None:
        """Initialize the SHA-256 class with initial hash values."""
        self.h: List[int] = [
            0x6A09E667,
            0xBB67AE85,
            0x3C6EF372,
            0xA54FF53A,
            0x510E527F,
            0x9B05688C,
            0x1F83D9AB,
            0x5BE0CD19,
        ]

    @staticmethod
    def _right_rotate(value: int, shift: int) -> int:
        """Rotate the bits of the value to the right by the specified shift."""
        return (value >> shift) | (value << (32 - shift)) & 0xFFFFFFFF

    def _compress(self, chunk: bytes) -> None:
        """Process a 512-bit chunk of the message."""
        w: List[int] = list(
            int.from_bytes(chunk[i : i + 4], "big") for i in range(0, 64, 4)
        )
        w += [0] * 48

        for i in range(16, 64):
            s0 = (
                self._right_rotate(w[i - 15], 7)
                ^ self._right_rotate(w[i - 15], 18)
                ^ (w[i - 15] >> 3)
            )
            s1 = (
                self._right_rotate(w[i - 2], 17)
                ^ self._right_rotate(w[i - 2], 19)
                ^ (w[i - 2] >> 10)
            )
            w[i] = (w[i - 16] + s0 + w[i - 7] + s1) & 0xFFFFFFFF

        a, b, c, d, e, f, g, h = self.h

        for i in range(64):
            S1 = (
                self._right_rotate(e, 6)
                ^ self._right_rotate(e, 11)
                ^ self._right_rotate(e, 25)
            )
            ch = (e & f) ^ (~e & g)
            temp1 = (h + S1 + ch + self.K[i] + w[i]) & 0xFFFFFFFF
            S0 = (
                self._right_rotate(a, 2)
                ^ self._right_rotate(a, 13)
                ^ self._right_rotate(a, 22)
            )
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xFFFFFFFF

            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF

        self.h[0] = (self.h[0] + a) & 0xFFFFFFFF
        self.h[1] = (self.h[1] + b) & 0xFFFFFFFF
        self.h[2] = (self.h[2] + c) & 0xFFFFFFFF
        self.h[3] = (self.h[3] + d) & 0xFFFFFFFF
        self.h[4] = (self.h[4] + e) & 0xFFFFFFFF
        self.h[5] = (self.h[5] + f) & 0xFFFFFFFF
        self.h[6] = (self.h[6] + g) & 0xFFFFFFFF
        self.h[7] = (self.h[7] + h) & 0xFFFFFFFF

    def hash(self, message: bytes) -> str:
        """
        Compute the SHA-256 hash of the input message.

        Args:
            message (bytes): The input message to hash.

        Returns:
            str: The SHA-256 hash as a hexadecimal string.
        """
        if not isinstance(message, bytes):
            raise TypeError("Input must be of type bytes.")

        # Pre-processing
        length = len(message) * 8
        message += b"\x80"
        while (len(message) + 8) % 64 != 0:
            message += b"\x00"
        message += length.to_bytes(8, "big")

        # Process the message in 512-bit chunks
        for i in range(0, len(message), 64):
            self._compress(message[i : i + 64])

        # Produce the final hash value
        return "".join(f"{x:08x}" for x in self.h)
