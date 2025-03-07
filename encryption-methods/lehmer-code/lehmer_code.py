from typing import List


class LehmerCode:
    """
    A class to handle Lehmer code encryption and decryption.
    """

    @staticmethod
    def encrypt(perm: List[int]) -> List[int]:
        """
        Encodes a permutation into its Lehmer code.

        Args:
            perm (List[int]): A list of integers representing a permutation.

        Returns:
            List[int]: The Lehmer code of the permutation.

        Raises:
            ValueError: If the input is not a valid permutation.
        """
        if not LehmerCode._is_valid_permutation(perm):
            raise ValueError("Input is not a valid permutation.")

        n = len(perm)
        lehmer = []
        for i in range(n):
            count = 0
            for j in range(i + 1, n):
                if perm[j] < perm[i]:
                    count += 1

            lehmer.append(count)

        return lehmer

    @staticmethod
    def decrypt(lehmer: List[int]) -> List[int]:
        """
        Decodes a Lehmer code back into the original permutation.

        Args:
            lehmer (List[int]): A list of integers representing the Lehmer code.

        Returns:
            List[int]: The original permutation.

        Raises:
            ValueError: If the input is not a valid Lehmer code.
        """
        if not LehmerCode._is_valid_lehmer_code(lehmer):
            raise ValueError("Input is not a valid Lehmer code.")

        n = len(lehmer)
        perm = []
        elements = list(range(1, n + 1))

        for i in range(n):
            index = lehmer[i]
            perm.append(elements.pop(index))

        return perm

    @staticmethod
    def _is_valid_permutation(perm: List[int]) -> bool:
        """
        Checks if the input is a valid permutation of integers.

        Args:
            perm (List[int]): A list of integers to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        return sorted(perm) == list(range(1, len(perm) + 1))

    @staticmethod
    def _is_valid_lehmer_code(lehmer: List[int]) -> bool:
        """
        Checks if the input is a valid Lehmer code.

        Args:
            lehmer (List[int]): A list of integers to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        n = len(lehmer)
        return all(0 <= code < n - i for i, code in enumerate(lehmer))
