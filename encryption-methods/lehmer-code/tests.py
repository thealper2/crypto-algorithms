import unittest
from lehmer_code import LehmerCode


class TestLehmerCode(unittest.TestCase):
    """
    Test suite for the LehmerCode class.
    This includes tests for both encryption and decryption functionalities.
    """

    def test_lehmer_code_encryption_valid_input(self):
        """
        Test Lehmer code encryption with a valid permutation.
        Expected result: Correct Lehmer code for the given permutation.
        """
        perm = [3, 1, 2]
        expected_lehmer = [2, 0, 0]
        result = LehmerCode.encrypt(perm)
        self.assertEqual(
            result, expected_lehmer, "Lehmer code encryption failed for valid input."
        )

    def test_lehmer_code_encryption_invalid_input(self):
        """
        Test Lehmer code encryption with an invalid permutation.
        Expected result: ValueError should be raised.
        """
        perm = [3, 1, 4]  # Invalid permutation (4 is out of range for n=3)
        with self.assertRaises(
            ValueError,
            msg="Lehmer code encryption did not raise ValueError for invalid input.",
        ):
            LehmerCode.encrypt(perm)

    def test_lehmer_code_decryption_valid_input(self):
        """
        Test Lehmer code decryption with a valid Lehmer code.
        Expected result: Correct permutation for the given Lehmer code.
        """
        lehmer = [2, 0, 0]
        expected_perm = [3, 1, 2]
        result = LehmerCode.decrypt(lehmer)
        self.assertEqual(
            result, expected_perm, "Lehmer code decryption failed for valid input."
        )

    def test_lehmer_code_decryption_invalid_input(self):
        """
        Test Lehmer code decryption with an invalid Lehmer code.
        Expected result: ValueError should be raised.
        """
        lehmer = [2, 0, 3]  # Invalid Lehmer code (3 is out of range for n=3)
        with self.assertRaises(
            ValueError,
            msg="Lehmer code decryption did not raise ValueError for invalid input.",
        ):
            LehmerCode.decrypt(lehmer)

    def test_lehmer_code_encryption_decryption_round_trip(self):
        """
        Test round-trip functionality: encrypting a permutation and then decrypting it.
        Expected result: The original permutation should be returned.
        """
        perm = [4, 2, 1, 3]
        lehmer = LehmerCode.encrypt(perm)
        result = LehmerCode.decrypt(lehmer)
        self.assertEqual(result, perm, "Round-trip encryption and decryption failed.")

    def test_lehmer_code_encryption_edge_case(self):
        """
        Test Lehmer code encryption with an edge case (single-element permutation).
        Expected result: Lehmer code should be [0].
        """
        perm = [1]
        expected_lehmer = [0]
        result = LehmerCode.encrypt(perm)
        self.assertEqual(
            result,
            expected_lehmer,
            "Lehmer code encryption failed for edge case (single-element permutation).",
        )

    def test_lehmer_code_decryption_edge_case(self):
        """
        Test Lehmer code decryption with an edge case (single-element Lehmer code).
        Expected result: Permutation should be [1].
        """
        lehmer = [0]
        expected_perm = [1]
        result = LehmerCode.decrypt(lehmer)
        self.assertEqual(
            result,
            expected_perm,
            "Lehmer code decryption failed for edge case (single-element Lehmer code).",
        )


if __name__ == "__main__":
    unittest.main()
