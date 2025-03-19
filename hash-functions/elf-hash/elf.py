from typing import Optional


class ElfHash:
    """
    A class to implement the Elf Hash algorithm.
    """

    def __init__(self):
        """
        Initialize the ElfHash class.
        """
        self.hash_value: int = 0  # Stores the computed hash value

    def compute_hash(self, input_string: str) -> int:
        """
        Compute the Elf Hash for a given input string.

        Args:
            input_string (str): The string to hash.

        Returns:
            int: The computed hash value.

        Raises:
            ValueError: If the input string is empty.
        """
        if not input_string:
            raise ValueError("Input string cannot be empty.")

        self.hash_value = 0  # Reset hash value for each computation

        for char in input_string:
            self.hash_value = (self.hash_value << 4) + ord(char)
            high_bits = self.hash_value & 0xF0000000  # Extract the top 4 bits

            if high_bits != 0:
                self.hash_value ^= (
                    high_bits >> 24
                )  # XOR with the top 4 bits shifted down

            self.hash_value &= ~high_bits  # Clear the top 4 bits

        return self.hash_value

    def get_hash(self) -> Optional[int]:
        """
        Get the last computed hash value.

        Returns:
            Optional[int]: The last computed hash value, or None if no hash has been computed yet.
        """
        return self.hash_value if self.hash_value != 0 else None
