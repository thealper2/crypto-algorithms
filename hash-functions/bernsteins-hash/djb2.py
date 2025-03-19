class DJB2Hash:
    """
    A class to implement Bernstein's Hash (DJB2) algorithm.
    """

    def __init__(self) -> None:
        """
        Initialize the DJB2Hash class.
        The initial hash value is set to 5381, a prime number commonly used in DJB2.
        """
        self.hash_value: int = 5381  # Initial hash value

    def update(self, data: str) -> None:
        """
        Update the hash value with the given data.

        Args:
            data (str): The input string to hash.

        Raises:
            TypeError: If the input data is not a string.
        """
        if not isinstance(data, str):
            raise TypeError("Input data must be a string.")

        for char in data:
            # Update the hash value using the DJB2 algorithm
            self.hash_value = ((self.hash_value << 5) + self.hash_value) + ord(char)

    def digest(self) -> int:
        """
        Return the final hash value as an integer.

        Returns:
            int: The computed hash value.
        """
        return self.hash_value

    def hexdigest(self) -> str:
        """
        Return the final hash value as a hexadecimal string.

        Returns:
            str: The computed hash value in hexadecimal format.
        """
        return hex(self.hash_value)
