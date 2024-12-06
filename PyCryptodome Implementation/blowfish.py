from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import time
import os

# Map Blowfish mode constants to their string representations
BLOWFISH_MODES = {
    Blowfish.MODE_CBC: "CBC",
    Blowfish.MODE_OFB: "OFB",
    Blowfish.MODE_CTR: "CTR",
}

def encrypt_blowfish(plaintext, key, mode, iv):
    """Encrypt plaintext using Blowfish."""
    if mode == Blowfish.MODE_CTR:
        # Use iv as the initial value for CTR mode with an empty nonce
        cipher = Blowfish.new(key, mode, nonce=b'', initial_value=iv)
        ciphertext = cipher.encrypt(plaintext)
    else:
        # Use iv as the Initialization Vector (IV) for CBC or OFB
        cipher = Blowfish.new(key, mode, iv=iv)
        ciphertext = cipher.encrypt(pad(plaintext, Blowfish.block_size))

    return ciphertext


def decrypt_blowfish(ciphertext, key, mode, iv):
    """Decrypt ciphertext using Blowfish."""
    if mode == Blowfish.MODE_CTR:
        # Use iv as the initial value for CTR mode with an empty nonce
        cipher = Blowfish.new(key, mode, nonce=b'', initial_value=iv)
        plaintext = cipher.decrypt(ciphertext)
    else:
        # Use iv as the Initialization Vector (IV) for CBC or OFB
        cipher = Blowfish.new(key, mode, iv=iv)
        plaintext = unpad(cipher.decrypt(ciphertext), Blowfish.block_size)

    return plaintext


def run_blowfish_tests(sample_plaintexts):
    """Run Blowfish encryption and decryption tests."""
    modes = [Blowfish.MODE_CBC, Blowfish.MODE_OFB, Blowfish.MODE_CTR]
    key_size = 16  # Default to 16 bytes (128 bits). Blowfish supports 32 to 448 bits.
    results = []

    for mode in modes:
        for plaintext_path in sample_plaintexts:
            plaintext_size = os.path.getsize(plaintext_path) // (1024 * 1024)  # MB
            with open(plaintext_path, 'rb') as f:
                plaintext = f.read()

            # Generate key and IV
            key = get_random_bytes(key_size)
            iv = get_random_bytes(Blowfish.block_size)  # Blowfish block size is 8 bytes

            # Encrypt the plaintext
            start_time = time.time()
            ciphertext = encrypt_blowfish(plaintext, key, mode, iv)
            encrypt_time = time.time() - start_time

            # Decrypt the ciphertext
            start_time = time.time()
            decrypted_plaintext = decrypt_blowfish(ciphertext, key, mode, iv)
            decrypt_time = time.time() - start_time

            # Verify correctness
            assert plaintext == decrypted_plaintext, "Decryption failed!"

            # Append results
            mode_name = BLOWFISH_MODES.get(mode, "Unknown Mode")
            results.append((mode_name, plaintext_size, key_size * 8, encrypt_time, decrypt_time))
            print(
                f"Blowfish | Mode: {mode_name} | Plaintext Size: {plaintext_size}MB | Key Size: {key_size * 8} bits | "
                f"Encrypt Time: {encrypt_time:.4f}s | Decrypt Time: {decrypt_time:.4f}s"
            )

    return results
