from typing import List


class TabulationHashing:
    """
    A class to implement Tabulation Hashing, a simple hashing technique that uses
    precomputed random tables for fast hashing of fixed-size keys.

    Attributes:
        table_size (int): The size of the hash table.
        random_tables (List[List[int]]): Precomputed random tables for hashing.
    """

    def __init__(self, table_size: int = 256, key_size: int = 8):
        """
        Initialize the TabulationHashing object.

        Args:
            table_size (int): The size of the hash table. Default is 256.
            key_size (int): The size of the key in bytes. Default is 8.
        """
        if table_size <= 0:
            raise ValueError("Table size must be a positive integer.")
        if key_size <= 0:
            raise ValueError("Key size must be a positive integer.")

        self.table_size = table_size
        self.key_size = key_size
        self.random_tables = self._generate_random_tables()

    def _generate_random_tables(self) -> List[List[int]]:
        """
        Generate random tables for tabulation hashing.

        Returns:
            List[List[int]]: A list of random tables, each containing `table_size` integers.
        """
        # For simplicity, we use a fixed seed to generate deterministic random tables.
        # In practice, you should use a cryptographically secure random generator.
        import random

        random.seed(42)

        tables = []
        for _ in range(self.key_size):
            table = [
                random.randint(0, self.table_size - 1) for _ in range(self.table_size)
            ]
            tables.append(table)
        return tables

    def hash(self, key: int) -> int:
        """
        Compute the hash value for a given key using tabulation hashing.

        Args:
            key (int): The key to hash. Must be a non-negative integer.

        Returns:
            int: The computed hash value.

        Raises:
            ValueError: If the key is negative or exceeds the maximum allowed size.
        """
        if key < 0:
            raise ValueError("Key must be a non-negative integer.")
        if key >= (1 << (self.key_size * 8)):
            raise ValueError("Key size exceeds the maximum allowed size.")

        hash_value = 0
        for i in range(self.key_size):
            # Extract the i-th byte of the key
            byte = (key >> (8 * i)) & 0xFF
            # XOR the byte with the corresponding value in the random table
            hash_value ^= self.random_tables[i][byte]
        return hash_value % self.table_size
