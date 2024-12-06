from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import time
import os

# Map AES mode constants to their string representations
AES_MODES = {
    AES.MODE_CBC: "CBC",
    AES.MODE_OFB: "OFB",
    AES.MODE_CTR: "CTR",
}

def encrypt_aes(plaintext, key, mode, iv):
    """Encrypt plaintext using AES."""
    if mode == AES.MODE_CTR:
        # Use iv as the initial value for CTR mode with an empty nonce
        cipher = AES.new(key, mode, nonce=b'', initial_value=iv)
        ciphertext = cipher.encrypt(plaintext)
    else:
        # Use iv as the Initialization Vector (IV) for CBC or OFB
        cipher = AES.new(key, mode, iv=iv)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    return ciphertext


def decrypt_aes(ciphertext, key, mode, iv):
    """Decrypt ciphertext using AES."""
    if mode == AES.MODE_CTR:
        # Use iv as the initial value for CTR mode with an empty nonce
        cipher = AES.new(key, mode, nonce=b'', initial_value=iv)
        plaintext = cipher.decrypt(ciphertext)
    else:
        # Use iv as the Initialization Vector (IV) for CBC or OFB
        cipher = AES.new(key, mode, iv=iv)
        plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    return plaintext


def run_aes_tests(sample_plaintexts):
    """Run AES encryption and decryption tests."""
    modes = [AES.MODE_CBC, AES.MODE_OFB, AES.MODE_CTR]
    key_sizes = [16, 24, 32]  # AES key sizes: 128, 192, 256 bits
    results = []

    for key_size in key_sizes:
        for mode in modes:
            for plaintext_path in sample_plaintexts:
                plaintext_size = os.path.getsize(plaintext_path) // (1024 * 1024)  # MB
                with open(plaintext_path, 'rb') as f:
                    plaintext = f.read()

                # Generate key and IV
                key = get_random_bytes(key_size)
                iv = get_random_bytes(AES.block_size)  # Ensure 16 bytes for AES block size

                # Encrypt the plaintext
                start_time = time.time()
                ciphertext = encrypt_aes(plaintext, key, mode, iv)
                encrypt_time = time.time() - start_time

                # Decrypt the ciphertext
                start_time = time.time()
                decrypted_plaintext = decrypt_aes(ciphertext, key, mode, iv)
                decrypt_time = time.time() - start_time

                # Verify correctness
                assert plaintext == decrypted_plaintext, "Decryption failed!"

                # Append results
                mode_name = AES_MODES.get(mode, "Unknown Mode")
                results.append((key_size * 8, mode_name, plaintext_size, encrypt_time, decrypt_time))
                print(
                    f"AES | Key Size: {key_size * 8} bits | Mode: {mode_name} | Plaintext Size: {plaintext_size}MB | "
                    f"Encrypt Time: {encrypt_time:.4f}s | Decrypt Time: {decrypt_time:.4f}s"
                )

    return results
