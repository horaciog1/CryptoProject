from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
import time
import os
from modes.cbc import cbc_encrypt, cbc_decrypt
from modes.ofb import ofb_encrypt, ofb_decrypt
from modes.ctr import ctr_encrypt_decrypt

def run_blowfish_tests(sample_plaintexts):
    """Run Blowfish encryption and decryption tests with custom modes."""
    block_size = 8  # Blowfish block size is 8 bytes
    key_size = 16   # Use a 128-bit (16-byte) key for this implementation
    key = get_random_bytes(key_size)  # Generate a random key
    iv = get_random_bytes(block_size)  # Generate a random IV
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)  # Create a cipher object with the key and ECB mode

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
                f"Blowfish | Mode: {mode_name} | Plaintext Size: {plaintext_size}MB | Key Size: {key_size * 8} bits | "
                f"Encrypt Time: {encrypt_time:.4f}s | Decrypt Time: {decrypt_time:.4f}s"
            )

# from Crypto.Cipher import Blowfish
# from Crypto.Random import get_random_bytes
# import time
# import os
# from modes.cbc import cbc_encrypt, cbc_decrypt
# from modes.ofb import ofb_encrypt, ofb_decrypt
# from modes.ctr import ctr_encrypt_decrypt_serial, ctr_encrypt_decrypt_parallel

# def run_blowfish_tests(sample_plaintexts):
#     """Run Blowfish encryption and decryption tests with custom modes."""
#     block_size = 8  # Blowfish block size is 8 bytes
#     key_size = 16   # Use a 128-bit (16-byte) key for this implementation
#     key = get_random_bytes(key_size)  # Generate a random key
#     iv = get_random_bytes(block_size)  # Generate a random IV
#     cipher = Blowfish.new(key, Blowfish.MODE_ECB)  # Create a cipher object with the key and ECB mode

#     # Modes to test
#     modes = {
#         "CBC": (cbc_encrypt, cbc_decrypt),
#         "OFB": (ofb_encrypt, ofb_decrypt),
#     }

#     # Add CTR modes (serial and parallel)
#     ctr_modes = {
#         "CTR (Serial)": ctr_encrypt_decrypt_serial,
#         "CTR (Parallel)": ctr_encrypt_decrypt_parallel,
#     }

#     print("Running Blowfish tests...")
#     for plaintext_path in sample_plaintexts:
#         # Get the plaintext size in MB
#         plaintext_size = os.path.getsize(plaintext_path) // (1024 * 1024)
#         with open(plaintext_path, 'rb') as f:
#             plaintext = f.read()

#         # Test block modes (CBC, OFB)
#         for mode_name, (encrypt_func, decrypt_func) in modes.items():
#             # Measure encryption time
#             start_time = time.time()
#             ciphertext = encrypt_func(plaintext, key, iv, block_size, cipher)
#             encrypt_time = time.time() - start_time

#             # Measure decryption time
#             start_time = time.time()
#             decrypted_text = decrypt_func(ciphertext, key, iv, block_size, cipher)
#             decrypt_time = time.time() - start_time

#             # Validate correctness
#             assert plaintext == decrypted_text, f"Decryption failed for mode {mode_name}!"

#             # Print formatted results
#             print(
#                 f"Blowfish | Mode: {mode_name} | Plaintext Size: {plaintext_size}MB | Key Size: {key_size * 8} bits | "
#                 f"Encrypt Time: {encrypt_time:.4f}s | Decrypt Time: {decrypt_time:.4f}s"
#             )

#         # Test CTR modes (serial and parallel)
#         for mode_name, ctr_func in ctr_modes.items():
#             # Measure encryption/decryption time (CTR is symmetric for both)
#             start_time = time.time()
#             result = ctr_func(plaintext, key, iv, block_size, cipher)
#             encrypt_time_ctr = time.time() - start_time

#             # Validate correctness (encrypt-decrypt symmetry)
#             start_time = time.time()
#             decrypted_text = ctr_func(result, key, iv, block_size, cipher)
#             decrypt_time_ctr = time.time() - start_time

#             assert plaintext == decrypted_text, f"Decryption failed for mode {mode_name}!"

#             # Print formatted results
#             print(
#                 f"Blowfish | Mode: {mode_name} | Plaintext Size: {plaintext_size}MB | Key Size: {key_size * 8} bits | "
#                 f"Encrypt Time: {encrypt_time_ctr:.4f}s | Decrypt Time: {decrypt_time_ctr:.4f}s"
#             )
