class XOR8:
    """
    A class to perform an 8-bit XOR operation on two binary strings.
    """

    def __init__(self, binary1: str, binary2: str):
        """
        Initialize the XOR8 class with two 8-bit binary strings.

        Args:
            binary1 (str): The first 8-bit binary string.
            binary2 (str): The second 8-bit binary string.

        Raises:
            ValueError: If the input strings are not 8-bit binary strings.
        """
        if not self._is_valid_binary(binary1) or not self._is_valid_binary(binary2):
            raise ValueError("Both inputs must be 8-bit binary strings.")

        self.binary1 = binary1
        self.binary2 = binary2

    @staticmethod
    def _is_valid_binary(binary: str) -> bool:
        """
        Check if the input is a valid 8-bit binary string.

        Args:
            binary (str): The binary string to validate.

        Returns:
            bool: True if theh input is a valid 8-bit binary string, False otherwise.
        """
        return len(binary) == 8 and all(bit in ("0", "1") for bit in binary)

    def perform_xor(self) -> str:
        """
        Perform the XOR operation on the two 8-bit binary strings.

        Returns:
            str: The result of the XOR operation as an 8-bit binary string.
        """
        result = []
        for bit1, bit2 in zip(self.binary1, self.binary2):
            # XOR Logic: If bits are different, result is '1'; otherwise, '0'.
            result.append("1" if bit1 != bit2 else "0")

        return "".join(result)
