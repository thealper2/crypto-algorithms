class Base58Cipher:
    """
    A class to encode and decode data using the Base58 algorithm.
    """

    # Base58 character set
    BASE58_CHARS = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    def __init__(self):
        """
        Initialize the Base58 encoder/decoder.
        """
        # Create a mapping from characters to their index in the BASE58_CHARS string
        self.char_to_index = {char: idx for idx, char in enumerate(self.BASE58_CHARS)}

    def encode(self, data: bytes) -> str:
        """
        Encode a byte array into a Base58 string.

        Args:
            data (bytes): The byte array to encode.

        Returns:
            str: The Base58 encoded string.

        Raises:
            ValueError: If the input data is empty.
        """
        if not data:
            raise ValueError("Input data cannot be empty.")

        # Count leading zeros
        leading_zeros = 0
        for byte in data:
            if byte == 0:
                leading_zeros += 1
            else:
                break

        # Convert bytes to a big integer
        num = int.from_bytes(data, byteorder="big")

        # Encode the number into Base58
        encoded = []
        while num > 0:
            num, remainder = divmod(num, 58)
            encoded.append(self.BASE58_CHARS[remainder])

        # Add leading '1's for each leading zero byte
        encoded.extend(["1"] * leading_zeros)

        # Reverse the list to get the final encoded string
        return "".join(reversed(encoded))

    def decode(self, encoded: str) -> bytes:
        """
        Decode a Base58 string into a byte array.

        Args:
            encoded (str): The Base58 string to decode.

        Returns:
            str: The decoded byte array.

        Raises:
            ValueError: If the input string contains invalid Base58 characters.
        """
        if not encoded:
            raise ValueError("Input string cannot be empty.")

        # Convert the Base58 string to a big integer
        num = 0
        for char in encoded:
            if char not in self.char_to_index:
                raise ValueError(f"Invalid Base58 character: {char}")
            num = num * 58 + self.char_to_index[char]

        # Convert the integer to bytes
        decoded_bytes = num.to_bytes((num.bit_length() + 7) // 8, byteorder="big")

        # Add leading zeros for each leading '1' in the Base58 string
        leading_ones = 0
        for char in encoded:
            if char == "1":
                leading_ones += 1
            else:
                break

        return bytes([0] * leading_ones) + decoded_bytes
