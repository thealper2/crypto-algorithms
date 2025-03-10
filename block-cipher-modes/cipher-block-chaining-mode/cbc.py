import argparse


class CBC:
    """
    A class to implement the Cipher Block Chaining (CBC) mode for block ciphers.
    """

    def __init__(self, block_size: int = 8):
        """
        Initialize the CBC mode with a specified block size.

        Args:
            block_size (int): The size of each block in bytes (default is 8 bytes).

        Raises:
            ValueError: If the block size is not a positive integer.
        """
        if block_size <= 0:
            raise ValueError("Block size must be a positive integer.")
        self.block_size = block_size

    def encrypt(self, plaintext: bytes, key: bytes, iv: bytes) -> bytes:
        """
        Encrypt the plaintext using CBC mode.

        Args:
            plaintext (bytes): The plaintext to encrypt, as bytes.
            key (bytes): The encryption key, as bytes.
            iv (bytes): The initialization vector (IV), as bytes. Must be the same size as the block size.

        Returns:
            bytes: The encrypted ciphertext, as bytes.

        Raises:
            ValueError: If the plaintext, key, or IV is empty, or if the plaintext length is not a multiple of the block size.
        """
        if not plaintext:
            raise ValueError("Plaintext cannot be empty.")
        if not key:
            raise ValueError("Key cannot be empty.")
        if not iv:
            raise ValueError("IV cannot be empty.")
        if len(iv) != self.block_size:
            raise ValueError(
                f"IV length must be equal to the block size ({self.block_size} bytes)."
            )
        if len(plaintext) % self.block_size != 0:
            raise ValueError(
                f"Plaintext length must be a multiple of the block size ({self.block_size} bytes)."
            )

        ciphertext = bytearray()
        previous_block = iv  # Initialize with IV

        for i in range(0, len(plaintext), self.block_size):
            block = plaintext[i : i + self.block_size]
            # XOR the current block with the previous ciphertext block (or IV for the first block)
            xor_block = bytes([b ^ p for b, p in zip(block, previous_block)])
            # Encrypt the XORed block
            encrypted_block = self._encrypt_block(xor_block, key)
            ciphertext.extend(encrypted_block)
            previous_block = encrypted_block  # Update the previous block

        return bytes(ciphertext)

    def decrypt(self, ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
        """
        Decrypt the ciphertext using CBC mode.

        Args:
            ciphertext (bytes): The ciphertext to decrypt, as bytes.
            key (bytes): The decryption key, as bytes.
            iv (bytes): The initialization vector (IV), as bytes. Must be the same size as the block size.

        Returns:
            bytes: The decrypted plaintext, as bytes.

        Raises:
            ValueError: If the ciphertext, key, or IV is empty, or if the ciphertext length is not a multiple of the block size.
        """
        if not ciphertext:
            raise ValueError("Ciphertext cannot be empty.")
        if not key:
            raise ValueError("Key cannot be empty.")
        if not iv:
            raise ValueError("IV cannot be empty.")
        if len(iv) != self.block_size:
            raise ValueError(
                f"IV length must be equal to the block size ({self.block_size} bytes)."
            )
        if len(ciphertext) % self.block_size != 0:
            raise ValueError(
                f"Ciphertext length must be a multiple of the block size ({self.block_size} bytes)."
            )

        plaintext = bytearray()
        previous_block = iv  # Initialize with IV

        for i in range(0, len(ciphertext), self.block_size):
            block = ciphertext[i : i + self.block_size]
            # Decrypt the current block
            decrypted_block = self._decrypt_block(block, key)
            # XOR the decrypted block with the previous ciphertext block (or IV for the first block)
            xor_block = bytes([d ^ p for d, p in zip(decrypted_block, previous_block)])
            plaintext.extend(xor_block)
            previous_block = block  # Update the previous block

        return bytes(plaintext)

    def _encrypt_block(self, block: bytes, key: bytes) -> bytes:
        """
        Encrypt a single block of plaintext using a simple XOR operation with the key.
        This is a placeholder for a real block cipher encryption function.

        Args:
            block (bytes): The block to encrypt, as bytes.
            key (bytes): The encryption key, as bytes.

        Returns:
            bytes: The encrypted block, as bytes.
        """
        return bytes([b ^ k for b, k in zip(block, key)])

    def _decrypt_block(self, block: bytes, key: bytes) -> bytes:
        """
        Decrypt a single block of ciphertext using a simple XOR operation with the key.
        This is a placeholder for a real block cipher decryption function.

        Args:
            block (bytes): The block to decrypt, as bytes.
            key (bytes): The decryption key, as bytes.

        Returns:
            bytes: The decrypted block, as bytes.
        """
        return bytes([b ^ k for b, k in zip(block, key)])


def main():
    """
    Main function to handle command-line arguments and demonstrate CBC encryption and decryption.
    """
    parser = argparse.ArgumentParser(
        description="Cipher Block Chaining (CBC) Mode Implementation"
    )
    parser.add_argument("--encrypt", action="store_true", help="Perform encryption")
    parser.add_argument("--decrypt", action="store_true", help="Perform decryption")
    parser.add_argument("--plaintext", type=str, help="Plaintext to encrypt")
    parser.add_argument("--ciphertext", type=str, help="Ciphertext to decrypt")
    parser.add_argument(
        "--key", type=str, required=True, help="Encryption/Decryption key"
    )
    parser.add_argument(
        "--iv", type=str, required=True, help="Initialization Vector (IV)"
    )
    parser.add_argument(
        "--block_size", type=int, default=8, help="Block size in bytes (default: 8)"
    )

    args = parser.parse_args()

    if not (args.encrypt or args.decrypt):
        parser.error("Please specify either --encrypt or --decrypt.")

    cbc = CBC(block_size=args.block_size)

    try:
        if args.encrypt:
            if not args.plaintext:
                parser.error("--plaintext is required for encryption.")
            plaintext = args.plaintext.encode()
            key = args.key.encode()
            iv = args.iv.encode()
            ciphertext = cbc.encrypt(plaintext, key, iv)
            print(f"Ciphertext: {ciphertext.hex()}")

        if args.decrypt:
            if not args.ciphertext:
                parser.error("--ciphertext is required for decryption.")
            ciphertext = bytes.fromhex(args.ciphertext)
            key = args.key.encode()
            iv = args.iv.encode()
            plaintext = cbc.decrypt(ciphertext, key, iv)
            print(f"Plaintext: {plaintext.decode()}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
