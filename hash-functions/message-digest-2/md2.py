from typing import List


class MD2:
    """
    A Python implementation of the MD2 hashing algorithm.
    """

    # MD2 Constants
    S = [
        41, 46, 67, 201, 162, 216, 124, 1, 61, 54, 84, 161, 236, 240, 6, 19,
        98, 167, 5, 243, 192, 199, 115, 140, 152, 147, 43, 217, 188, 76, 130, 202,
        30, 155, 87, 60, 253, 212, 224, 22, 103, 66, 111, 24, 138, 23, 229, 18,
        190, 78, 196, 214, 218, 158, 222, 73, 160, 251, 245, 142, 187, 47, 238, 122,
        169, 104, 121, 145, 21, 178, 7, 63, 148, 194, 16, 137, 11, 34, 95, 33,
        128, 127, 93, 154, 90, 144, 50, 39, 53, 62, 204, 231, 191, 247, 151, 3,
        255, 25, 48, 179, 72, 165, 181, 209, 215, 94, 146, 42, 172, 86, 170, 198,
        79, 184, 56, 210, 150, 164, 125, 182, 118, 252, 107, 226, 156, 116, 4, 241,
        69, 157, 112, 89, 100, 113, 135, 32, 134, 91, 207, 101, 230, 45, 168, 2,
        27, 96, 37, 173, 174, 176, 185, 246, 28, 70, 97, 105, 52, 64, 126, 15,
        85, 71, 163, 35, 221, 81, 175, 58, 195, 92, 249, 206, 186, 197, 234, 38,
        44, 83, 13, 110, 133, 40, 132, 9, 211, 223, 205, 244, 65, 129, 77, 82,
        106, 220, 55, 200, 108, 193, 171, 250, 36, 225, 123, 8, 12, 189, 177, 74,
        120, 136, 149, 139, 227, 99, 232, 109, 233, 203, 213, 254, 59, 0, 29, 57,
        242, 239, 183, 14, 102, 88, 208, 228, 166, 119, 114, 248, 235, 117, 75, 10,
        49, 68, 80, 180, 143, 237, 31, 26, 219, 153, 141, 51, 159, 17, 131, 20
    ]
    def __init__(self) -> None:
        """
        Initialize the MD2 object.

        Attributes:
            state (List[int]): 48-byte buffer.
            checksum (List[int]): 16-byte checksum.
            buffer (List[int]): Input buffer.
        """
        self.state: List[int] = [0] * 48
        self.checksum: List[int] = [0] * 16
        self.buffer: List[int] = []

    def _pad_message(self, message: bytes) -> bytes:
        """
        Pad the message according to the MD2 specification.

        Args:
            message (bytes): The input message to pad.

        Returns:
            bytes: The padded message
        """
        padding_length = 16 - (len(message) % 16)
        padding = bytes([padding_length] * padding_length)
        return message + padding

    def _update_checksum(self, block: List[int]) -> None:
        """
        Update the checksum based on the current block.

        Args:
            block (List[int]): The current 16-byte block.
        """
        x = self.checksum[-1]
        for i in range(16):
            x = self.S[block[i] ^ x] ^ self.checksum[i]
            self.checksum[i] = x

    def _process_block(self, block: List[int]) -> None:
        """
        Process a single 16-byte block.

        Args:
            block (List[int]): The 16-byte block to process.
        """
        # Update the state
        for i in range(16):
            self.state[i + 16] = block[i]
            self.state[i + 32] = self.state[i + 16] ^ self.state[i]

        t = 0
        for i in range(18):
            for j in range(48):
                self.state[j] ^= self.S[t]
                t = self.state[j]

            t = (t + i) % 256

    def hash(self, message: bytes) -> str:
        """
        Compute the MD2 hash of the input message.

        Args:
            message (bytes): The input message to hash.

        Returns:
            str: The MD2 hash as a hexadecimal string.
        """
        if not isinstance(message, bytes):
            raise TypeError("Input message must be of type bytes.")

        # Step 1: Pad the message
        padded_message = self._pad_message(message)

        # Step 2: Process each 16-byte block
        for i in range(0, len(padded_message), 16):
            block = list(padded_message[i : i + 16])
            self._process_block(block)
            self._update_checksum(block)

        # Step 3: Append the checksum as a final block
        self._process_block(self.checksum)

        # Step 4: The hash is the first 16 bytes of the state
        hash_bytes = bytes(self.state[:16])
        return hash_bytes.hex()
