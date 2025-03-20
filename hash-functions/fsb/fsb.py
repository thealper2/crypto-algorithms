from typing import List


class FSBHash:
    """
    Fast Syndrome-based Hash Function (FSB) implementation.

    Attributes:
        n (int): Length of the binary code.
        k (int): Length of the input message in bits.
        t (int): Number of ones in each row of the parity-check matrix H.
        H (List[List[int]]): Parity-check matrix.
    """

    def __init__(self, n: int, k: int, t: int) -> None:
        """
        Initializes the FSB hash function with the given parameters.

        Args:
            n (int): Length of the binary code.
            k (int): Length of the input message in bits.
            t (int): Number of ones in each row of the parity-check matrix H.
        """
        if t <= 0 or t > n:
            raise ValueError("Parameter t must be > 0 and <= n")
        if k <= 0:
            raise ValueError("Parameter k must be > 0")
        if n <= 0:
            raise ValueError("Parameter n must be > 0")

        self.n = n
        self.k = k
        self.t = t
        self.H = self.generate_parity_check_matrix()

    def generate_parity_check_matrix(self) -> List[List[int]]:
        """
        Generates a random parity-check matrix H of size k x n
        with t ones per row.

        Returns:
            List[List[int]]: The generated parity-check matrix.
        """
        from random import sample

        H = []
        for _ in range(self.k):
            row = [0] * self.n
            ones_indices = sample(range(self.n), self.t)
            for idx in ones_indices:
                row[idx] = 1
            H.append(row)
        return H

    def hash(self, message: List[int]) -> List[int]:
        """
        Computes the hash (syndrome) of the input message.

        Args:
            message (List[int]): The input message as a list of bits (0 or 1).

        Returns:
            List[int]: The syndrome (hash output).
        """
        if len(message) != self.n:
            raise ValueError(f"Message length must be {self.n} bits")
        if any(bit not in (0, 1) for bit in message):
            raise ValueError("Message must contain only 0s and 1s")

        syndrome = []
        for row in self.H:
            # Compute dot product modulo 2
            dot = sum([m * h for m, h in zip(message, row)]) % 2
            syndrome.append(dot)
        return syndrome

    def print_matrix(self) -> None:
        """Prints the parity-check matrix H."""
        for row in self.H:
            print("".join(str(bit) for bit in row))
