from typing import List


class CRC:
    """
    A class to implement Cyclic Redundancy Check (CRC) algorithm.
    """

    def __init__(
        self,
        polynomial: int,
        initial_value: int = 0xFFFF,
        final_xor_value: int = 0x0000,
    ):
        """
        Initialize the CRC object with the given polynomial, initial value and final XOR value.

        Attributes:
            polynomial (int): The polynomial to use for CRC calculation. This should be an integer representing the polynomial.
            initial_value (int): The initial value for the CRC calculation. Default is 0xFFFF.
            final_xor_value (int): The value to XOR with the final CRC value. Default is 0x0000.
        """
        self.polynomial = polynomial
        self.initial_value = initial_value
        self.final_xor_value = final_xor_value

    def calculate_crc(self, data: List[int]) -> int:
        """
        Calculate the CRC value for the given data.

        Args:
            data (List[int]): A list of integers representing te data bytes.

        Returns:
            int: The calculated CRC value as integer.
        """
        crc = self.initial_value

        for byte in data:
            crc ^= byte << 8
            for _ in range(8):
                if crc & 0x8000:
                    crc = (crc << 1) ^ self.polynomial
                else:
                    crc <<= 1

                crc &= 0xFFFF  # Ensure CRC remains 16 bit

        return crc ^ self.final_xor_value

    @staticmethod
    def hex_string_to_bytes(hex_str: str) -> List[int]:
        """
        Convert a hex string to a list of integers representing bytes.

        Args:
            hex_str (str): A string representing the data in hexadecimal format.

        Returns:
            List[int]: A list of integers representing the bytes.
        """
        if len(hex_str) % 2 != 0:
            raise ValueError("Hex string must have an even number of characters")

        try:
            return [int(hex_str[i : i + 2], 16) for i in range(0, len(hex_str), 2)]
        except ValueError as e:
            raise ValueError("Invalid hex string") from e
