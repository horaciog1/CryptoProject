from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import time
import os
from modes.cbc import cbc_encrypt, cbc_decrypt
from modes.ofb import ofb_encrypt, ofb_decrypt
from modes.ctr import ctr_encrypt_decrypt

def run_3des_tests(sample_plaintexts):
    """Run 3DES encryption and decryption tests with custom modes."""
    block_size = 8  # 3DES block size is 8 bytes
    key_size = 24   # 3DES key size is 24 bytes (3 keys of 8 bytes each)
    key = DES3.adjust_key_parity(get_random_bytes(key_size))  # Generate a random 24-byte key with parity
    iv = get_random_bytes(block_size)  # Generate a random IV
    cipher = DES3.new(key, DES3.MODE_ECB)  # Create a cipher object with the key and ECB mode

    # Modes to test
    modes = {
        "CBC": (cbc_encrypt, cbc_decrypt),
        "OFB": (ofb_encrypt, ofb_decrypt),
        "CTR": (ctr_encrypt_decrypt, ctr_encrypt_decrypt),
    }

    for plaintext_path in sample_plaintexts:
        # Get the plaintext size in MB
        plaintext_size = os.path.getsize(plaintext_path) // (1024 * 1024)
        with open(plaintext_path, 'rb') as f:
            plaintext = f.read()

        for mode_name, (encrypt_func, decrypt_func) in modes.items():
            # Measure encryption time
            start_time = time.time()
            ciphertext = encrypt_func(plaintext, key, iv, block_size, cipher)
            encrypt_time = time.time() - start_time

            # Measure decryption time
            start_time = time.time()
            decrypted_text = decrypt_func(ciphertext, key, iv, block_size, cipher)
            decrypt_time = time.time() - start_time

            # Validate correctness
            assert plaintext == decrypted_text, f"Decryption failed for mode {mode_name}!"

            # Print formatted results
            print(
                f"3DES | Mode: {mode_name} | Plaintext Size: {plaintext_size}MB | Key Size: {key_size * 8} bits | "
                f"Encrypt Time: {encrypt_time:.4f}s | Decrypt Time: {decrypt_time:.4f}s"
            )
