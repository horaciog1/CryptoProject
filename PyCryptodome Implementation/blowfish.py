from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import time
import os  # Add this import

def encrypt_blowfish(plaintext, key, mode, iv=None):
    """Encrypt plaintext using Blowfish."""
    cipher = Blowfish.new(key, mode, iv=iv)
    ciphertext = cipher.encrypt(pad(plaintext, Blowfish.block_size))
    return ciphertext

def run_blowfish_tests(sample_plaintexts):
    """Run Blowfish encryption tests."""
    modes = [Blowfish.MODE_CBC, Blowfish.MODE_OFB, Blowfish.MODE_CTR]
    key_size = 16  # Blowfish supports key sizes from 32 to 448 bits
    results = []

    for mode in modes:
        for plaintext_path in sample_plaintexts:
            plaintext_size = os.path.getsize(plaintext_path) // (1024 * 1024)  # MB
            with open(plaintext_path, 'rb') as f:
                plaintext = f.read()

            key = get_random_bytes(key_size)
            iv = get_random_bytes(Blowfish.block_size) if mode != Blowfish.MODE_CTR else None

            start_time = time.time()
            encrypt_blowfish(plaintext, key, mode, iv)
            elapsed_time = time.time() - start_time

            results.append((mode, plaintext_size, elapsed_time))
            print(f"Blowfish | Mode: {mode} | Size: {plaintext_size}MB | Time: {elapsed_time:.4f}s")

    return results
