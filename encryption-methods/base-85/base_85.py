class Base85Cipher:
    """
    A class to handle Base85 encoding and decoding.
    """

    # Base85 character set
    _BASE85_CHARS = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstu"

    def __init__(self):
        """
        Initialize the Base85 encoder/decoder.
        """
        # Create a dictionary for quick lookup of character indices
        self._char_to_index = {char: idx for idx, char in enumerate(self._BASE85_CHARS)}

    def encode(self, data: bytes) -> str:
        """
        Encode binary data into a Base85 string.

        Args:
            data (bytes): Binary data to encode.

        Returns:
            str: Base85 encoded string.
        """
        if not isinstance(data, bytes):
            raise TypeError("Input data must be of type 'bytes'.")

        encoded = []
        padding = len(data) % 4
        if padding:
            data += b"\x00" * (4 - padding)  # Pad with zeros if necessary

        for i in range(0, len(data), 4):
            chunk = int.from_bytes(data[i : i + 4], "big")
            if chunk == 0:
                encoded.append("z")  # Special case for zero
                continue

            temp = []
            for _ in range(5):
                temp.append(self._BASE85_CHARS[chunk % 85])
                chunk = chunk // 85

            encoded.extend(reversed(temp))

        # Remove padding characters
        if padding:
            encoded = encoded[: -(4 - padding)]

        return "".join(encoded)

    def decode(self, encoded: str) -> bytes:
        """
        Decode a Base85 string into binary data.

        Args:
            encoded (str): Base85 encoded string.

        Returns:
            bytes: Decoded binary data.
        """
        if not isinstance(encoded, str):
            raise TypeError("Input data must be of type 'str'.")

        decoded = bytearray()
        padding = len(encoded) % 5
        if padding:
            encoded += "u" * (5 - padding)  # Pad with 'u' if necessary

        i = 0
        while i < len(encoded):
            if encoded[i] == "z":
                decoded.extend(b"\x00\x00\x00\x00")
                i += 1
                continue

            chunk = 0
            for j in range(5):
                if i + j >= len(encoded):
                    raise ValueError("Invalid Base85 string length.")
                char = encoded[i + j]
                if char not in self._char_to_index:
                    raise ValueError(f"Invalid Base85 character: {char}")
                chunk = chunk * 85 + self._char_to_index[char]

            decoded.extend(chunk.to_bytes(4, "big"))
            i += 5

        # Remove padding bytes
        if padding:
            decoded = decoded[: -(4 - padding)]

        return bytes(decoded)
