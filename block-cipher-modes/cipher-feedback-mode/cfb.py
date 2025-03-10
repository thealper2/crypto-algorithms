import argparse


class CFBMode:
    """
    Implements Cipher Feedback Mode (CFB) for block cipher encryption and decryption.
    """

    def __init__(self, key: bytes, iv: bytes, block_size: int = 16) -> None:
        """
        Initialize CFB Mode with a key, IV, and block size.

        Attributes:
            key (bytes): The encryption key as bytes.
            iv (bytes): The initialization vector as bytes.
            block_size (bytes): The block size in bytes (default: 16 bytes for AES).
        """
        if len(iv) != block_size:
            raise ValueError("IV length must match block size.")

        self.key = key
        self.iv = iv
        self.block_size = block_size

    def _dummy_block_cipher(self, block: bytes) -> bytes:
        """
        A dummy block cipher function (simple XOR with the key for demonstration).

        Args:
            block (bytes): The input block of plaintext.

        Returns:
            bytes: Encrypted block as bytes.
        """
        return bytes(b ^ k for b, k in zip(block, self.key))

    def encrypt(self, plaintext: bytes) -> bytes:
        """
        Encrypt data using CFB mode.

        Args:
            plaintext (bytes): The plaintext to encrypt.

        Returns:
            bytes: The encrypted ciphertext as bytes.
        """
        ciphertext = bytearray()
        feedback = self.iv

        for i in range(0, len(plaintext), self.block_size):
            block = plaintext[i : i + self.block_size]
            cipher_block = self._dummy_block_cipher(feedback)
            encrypted_block = bytes(b ^ c for b, c in zip(block, cipher_block))

            ciphertext.extend(encrypted_block)
            feedback = encrypted_block  # Update feedback with ciphertext

        return bytes(ciphertext)

    def decrypt(self, ciphertext: bytes) -> bytes:
        """
        Decrypt data using CFB mode.

        Args:
            ciphertext (bytes): The ciphertext to decrypt.

        Returns:
            bytes: The decrypted plaintext as bytes.
        """
        plaintext = bytearray()
        feedback = self.iv

        for i in range(0, len(ciphertext), self.block_size):
            block = ciphertext[i : i + self.block_size]
            cipher_block = self._dummy_block_cipher(feedback)
            decrypted_block = bytes(b ^ c for b, c in zip(block, cipher_block))

            plaintext.extend(decrypted_block)
            feedback = block  # Update feedback with ciphertext

        return bytes(plaintext)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CFB Mode Encryption & Decryption")
    parser.add_argument(
        "-k", "--key", type=str, required=True, help="Encryption key (hex format)"
    )
    parser.add_argument(
        "-iv",
        "--iv",
        type=str,
        required=True,
        help="Initialization vector (hex format)",
    )
    parser.add_argument(
        "-m",
        "--mode",
        choices=["encrypt", "decrypt"],
        required=True,
        help="Mode: encrypt or decrypt",
    )
    parser.add_argument(
        "-i", "--input", type=str, required=True, help="Input text (hex format)"
    )

    args = parser.parse_args()
    key = bytes.fromhex(args.key)
    iv = bytes.fromhex(args.iv)
    input_data = bytes.fromhex(args.input)

    cfb = CFBMode(key, iv)

    if args.mode == "encrypt":
        result = cfb.encrypt(input_data)
    else:
        result = cfb.decrypt(input_data)

    print("Output (hex):", result.hex())
