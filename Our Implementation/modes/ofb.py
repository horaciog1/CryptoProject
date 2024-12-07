# from utils import xor_bytes, split_blocks

# def ofb_encrypt(plaintext, key, iv, block_size, cipher):
#     """Custom OFB mode encryption."""
#     blocks = split_blocks(plaintext, block_size)
#     encrypted_blocks = []
#     current_iv = iv

#     for block in blocks:
#         # Encrypt the IV (feedback value)
#         encrypted_iv = cipher.encrypt(current_iv)
#         # XOR the plaintext block with the encrypted IV
#         encrypted_block = xor_bytes(block, encrypted_iv[:len(block)])
#         encrypted_blocks.append(encrypted_block)
#         # Update the feedback value
#         current_iv = encrypted_iv

#     return b''.join(encrypted_blocks)

# def ofb_decrypt(ciphertext, key, iv, block_size, cipher):
#     """Custom OFB mode decryption."""
#     # Decryption in OFB mode is the same as encryption
#     return ofb_encrypt(ciphertext, key, iv, block_size, cipher)

from utils import xor_bytes, split_blocks
from multiprocessing import Pool

def ofb_encrypt_serial(plaintext, key, iv, block_size, cipher):
    """Custom OFB mode encryption (serial version)."""
    blocks = split_blocks(plaintext, block_size)
    encrypted_blocks = []
    current_iv = iv

    for block in blocks:
        encrypted_iv = cipher.encrypt(current_iv)
        encrypted_block = xor_bytes(block, encrypted_iv[:len(block)])
        encrypted_blocks.append(encrypted_block)
        current_iv = encrypted_iv

    return b''.join(encrypted_blocks)

def ofb_encrypt_parallel(plaintext, key, iv, block_size, cipher):
    """Custom OFB mode encryption (parallel version)."""
    blocks = split_blocks(plaintext, block_size)

    # Precompute encrypted IVs in parallel
    def encrypt_iv_chain(index):
        feedback_iv = iv
        for _ in range(index):
            feedback_iv = cipher.encrypt(feedback_iv)
        return cipher.encrypt(feedback_iv)

    with Pool() as pool:
        encrypted_ivs = pool.map(encrypt_iv_chain, range(len(blocks)))

    # XOR plaintext with precomputed IVs
    encrypted_blocks = [xor_bytes(block, iv[:len(block)]) for block, iv in zip(blocks, encrypted_ivs)]

    return b''.join(encrypted_blocks)

def ofb_decrypt_serial(ciphertext, key, iv, block_size, cipher):
    """Custom OFB mode decryption (serial version)."""
    return ofb_encrypt_serial(ciphertext, key, iv, block_size, cipher)

def ofb_decrypt_parallel(ciphertext, key, iv, block_size, cipher):
    """Custom OFB mode decryption (parallel version)."""
    return ofb_encrypt_parallel(ciphertext, key, iv, block_size, cipher)
