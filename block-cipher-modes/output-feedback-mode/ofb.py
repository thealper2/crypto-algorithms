import argparse
from typing import List


class OFBMode:
    """
    A class to implement the Output Feedback Mode (OFB) for block ciphers.
    """

    def __init__(self, key: int, iv: int, block_size: int = 8):
        """
        Initialize the OFB mode with a key, initialization vector (IV), and block size.

        Attributes:
            key (int): The encryption key.
            iv (int): The initialization vector.
            block_size (int): The block size in bytes (default is 8 bytes).
        """
        if block_size <= 0:
            raise ValueError("Block size must be a positive integer.")
        if key < 0 or iv < 0:
            raise ValueError("Key and IV must be non-negative integers.")

        self.key = key
        self.iv = iv
        self.block_size = block_size

    def _encrypt_block(self, block: int) -> int:
        """
        Encrypt a single block using a simple XOR operation with the key.

        Args:
            block (int): The block to encrypt.

        Returns:
            int: The encrypted block.
        """
        return block ^ self.key

    def _split_into_blocks(self, data: bytes) -> List[int]:
        """
        Split the input data into blocks of the specified size.

        Args:
            data (bytes): The input data as bytes.

        Returns:
            bytes: A list of integers representing the blocks.
        """
        if len(data) % self.block_size != 0:
            raise ValueError("Data length must be a multiple of the block size.")
        return [
            int.from_bytes(data[i : i + self.block_size], "big")
            for i in range(0, len(data), self.block_size)
        ]

    def _merge_blocks(self, blocks: List[int]) -> bytes:
        """
        Merge a list of blocks into a single bytes object.

        Args:
            blocks (List[int]): A list of integers representing the blocks.

        Returns:
            bytes: The merged data as bytes.
        """
        return b"".join(block.to_bytes(self.block_size, "big") for block in blocks)

    def encrypt(self, plaintext: bytes) -> bytes:
        """
        Encrypt the plaintext using OFB mode.

        Args:
            plaintext (bytes): The plaintext data as bytes.

        Returns:
            bytes: The encrypted ciphertext as bytes.
        """
        blocks = self._split_into_blocks(plaintext)
        ciphertext_blocks = []
        previous_output = self.iv

        for block in blocks:
            encrypted_output = self._encrypt_block(previous_output)
            ciphertext_blocks.append(block ^ encrypted_output)
            previous_output = encrypted_output

        return self._merge_blocks(ciphertext_blocks)

    def decrypt(self, ciphertext: bytes) -> bytes:
        """
        Decrypt the ciphertext using OFB mode.

        Args:
            ciphertext (bytes): The ciphertext data as bytes.

        Returns:
            bytes: The decrypted plaintext as bytes.
        """
        # OFB mode decryption is the same as encryption
        return self.encrypt(ciphertext)


def main():
    """
    Main function to handle command-line arguments and demonstrate OFB mode.
    """
    parser = argparse.ArgumentParser(
        description="Output Feedback Mode (OFB) implementation for block ciphers."
    )
    parser.add_argument(
        "--key", type=int, required=True, help="Encryption key (integer)."
    )
    parser.add_argument(
        "--iv", type=int, required=True, help="Initialization vector (integer)."
    )
    parser.add_argument(
        "--block-size", type=int, default=8, help="Block size in bytes (default is 8)."
    )
    parser.add_argument(
        "--plaintext", type=str, required=True, help="Plaintext to encrypt."
    )
    args = parser.parse_args()

    try:
        # Initialize OFB mode
        ofb = OFBMode(key=args.key, iv=args.iv, block_size=args.block_size)

        # Encrypt the plaintext
        plaintext_bytes = args.plaintext.encode("utf-8")
        ciphertext = ofb.encrypt(plaintext_bytes)
        print(f"Ciphertext: {ciphertext.hex()}")

        # Decrypt the ciphertext
        decrypted_text = ofb.decrypt(ciphertext)
        print(f"Decrypted text: {decrypted_text.decode('utf-8')}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
