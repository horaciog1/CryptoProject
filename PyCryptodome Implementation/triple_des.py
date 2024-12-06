from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os
import time

# Map DES3 mode constants to their string representations
DES3_MODES = {
    DES3.MODE_CBC: "CBC",
    DES3.MODE_OFB: "OFB",
    DES3.MODE_CTR: "CTR",
}

def encrypt_3des(plaintext, key, mode, iv):
    """Encrypt plaintext using 3DES."""
    if mode == DES3.MODE_CTR:
        # Use iv as the initial value for CTR mode with an empty nonce
        cipher = DES3.new(key, mode, nonce=b'', initial_value=iv)
        ciphertext = cipher.encrypt(plaintext)
    else:
        # Use iv as the Initialization Vector (IV) for CBC or OFB
        cipher = DES3.new(key, mode, iv=iv)
        ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))

    return ciphertext


def decrypt_3des(ciphertext, key, mode, iv):
    """Decrypt ciphertext using 3DES."""
    if mode == DES3.MODE_CTR:
        # Use iv as the initial value for CTR mode with an empty nonce
        cipher = DES3.new(key, mode, nonce=b'', initial_value=iv)
        plaintext = cipher.decrypt(ciphertext)
    else:
        # Use iv as the Initialization Vector (IV) for CBC or OFB
        cipher = DES3.new(key, mode, iv=iv)
        plaintext = unpad(cipher.decrypt(ciphertext), DES3.block_size)

    return plaintext


def run_3des_tests(sample_plaintexts):
    """Run 3DES encryption and decryption tests."""
    modes = [DES3.MODE_CBC, DES3.MODE_OFB, DES3.MODE_CTR]
    key_size = 24  # 64 * 3 = 192 bits = 24 bytes = Using 3 keys of 64 bits each
    results = []

    for mode in modes:
        for plaintext_path in sample_plaintexts:
            plaintext_size = os.path.getsize(plaintext_path) // (1024 * 1024)  # MB
            with open(plaintext_path, 'rb') as f:
                plaintext = f.read()

            # Generate key and IV
            key = get_random_bytes(key_size)
            iv = get_random_bytes(DES3.block_size)  # 64-bit value for IV or counter initial value

            # Encrypt the plaintext
            start_time = time.time()
            ciphertext = encrypt_3des(plaintext, key, mode, iv)
            encrypt_time = time.time() - start_time

            # Decrypt the ciphertext
            start_time = time.time()
            decrypted_plaintext = decrypt_3des(ciphertext, key, mode, iv)
            decrypt_time = time.time() - start_time

            # Verify correctness
            assert plaintext == decrypted_plaintext, "Decryption failed!"

            # Append results
            mode_name = DES3_MODES.get(mode, "Unknown Mode")
            results.append((mode_name, plaintext_size, encrypt_time, decrypt_time))
            print(
                f"3DES | Mode: {mode_name} | Plaintext Size: {plaintext_size}MB | Key Size: {key_size * 8} bits | "
                f"Encrypt Time: {encrypt_time:.4f}s | Decrypt Time: {decrypt_time:.4f}s"
            )

    return results
