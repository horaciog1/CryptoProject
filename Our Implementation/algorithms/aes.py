from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import time
import os
from modes.cbc import cbc_encrypt, cbc_decrypt
# from modes.ofb import ofb_encrypt, ofb_decrypt
# from modes.ctr import ctr_encrypt_decrypt
from modes.ofb import ofb_encrypt_serial, ofb_encrypt_parallel, ofb_decrypt_serial, ofb_decrypt_parallel
from modes.ctr import ctr_encrypt_decrypt_serial, ctr_encrypt_decrypt_parallel

def run_aes_tests(sample_plaintexts):
    """Run AES encryption and decryption tests with 128, 192, and 256-bit keys."""
    block_size = 16  # AES block size is 16 bytes

    # Define key sizes for AES
    key_sizes = [16, 24, 32]  # 128-bit, 192-bit, and 256-bit keys

    # Modes to test
    # modes = {
    #     "CBC": (cbc_encrypt, cbc_decrypt),
    #     "OFB": (ofb_encrypt, ofb_decrypt),
    #     "CTR": (ctr_encrypt_decrypt, ctr_encrypt_decrypt),
    # }
    modes = {
        "CBC": (cbc_encrypt, cbc_decrypt, "serial"),  # CBC is always serial
        "OFB (Serial)": (ofb_encrypt_serial, ofb_decrypt_serial, "serial"),
        "OFB (Parallel)": (ofb_encrypt_parallel, ofb_decrypt_parallel, "parallel"),
        "CTR (Serial)": (ctr_encrypt_decrypt_serial, ctr_encrypt_decrypt_serial, "serial"),
        "CTR (Parallel)": (ctr_encrypt_decrypt_parallel, ctr_encrypt_decrypt_parallel, "parallel"),
    }

    for key_size in key_sizes:
        key = get_random_bytes(key_size)  # Generate a random key of the specified size
        iv = get_random_bytes(block_size)  # Generate a random IV
        cipher = AES.new(key, AES.MODE_ECB)  # Create a cipher object with the key and ECB mode

        # print(f"Testing AES with a {key_size * 8}-bit key...")
        # for plaintext_path in sample_plaintexts:
        #     # Get the plaintext size in MB
        #     plaintext_size = os.path.getsize(plaintext_path) // (1024 * 1024)
        #     with open(plaintext_path, 'rb') as f:
        #         plaintext = f.read()

        #     for mode_name, (encrypt_func, decrypt_func) in modes.items():
        #         # Measure encryption time
        #         start_time = time.time()
        #         ciphertext = encrypt_func(plaintext, key, iv, block_size, cipher)
        #         encrypt_time = time.time() - start_time

        #         # Measure decryption time
        #         start_time = time.time()
        #         decrypted_text = decrypt_func(ciphertext, key, iv, block_size, cipher)
        #         decrypt_time = time.time() - start_time

        #         # Validate correctness
        #         assert plaintext == decrypted_text, f"Decryption failed for mode {mode_name} with key size {key_size * 8} bits!"

        #         # Print formatted results
        #         print(
        #             f"AES-{key_size * 8} | Mode: {mode_name} | Plaintext Size: {plaintext_size}MB | Key Size: {key_size * 8} bits | "
        #             f"Encrypt Time: {encrypt_time:.4f}s | Decrypt Time: {decrypt_time:.4f}s"
        #         )
        print(f"Testing AES with a {key_size * 8}-bit key...")
        for plaintext_path in sample_plaintexts:
            plaintext_size = os.path.getsize(plaintext_path) // (1024 * 1024)
            with open(plaintext_path, 'rb') as f:
                plaintext = f.read()

            for mode_name, (encrypt_func, decrypt_func, parallelism) in modes.items():
                start_time = time.time()
                ciphertext = encrypt_func(plaintext, key, iv, block_size, cipher)
                encrypt_time = time.time() - start_time

                start_time = time.time()
                decrypted_text = decrypt_func(ciphertext, key, iv, block_size, cipher)
                decrypt_time = time.time() - start_time

                assert plaintext == decrypted_text, f"Decryption failed for {mode_name} with key size {key_size * 8} bits!"

                print(
                    f"AES-{key_size * 8} | Mode: {mode_name} | Parallel: {parallelism} | Plaintext Size: {plaintext_size}MB | "
                    f"Key Size: {key_size * 8} bits | Encrypt Time: {encrypt_time:.4f}s | Decrypt Time: {decrypt_time:.4f}s"
                )
