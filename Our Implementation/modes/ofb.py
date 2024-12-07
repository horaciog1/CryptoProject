from utils import xor_bytes, split_blocks

def ofb_encrypt(plaintext, key, iv, block_size, cipher):
    """Custom OFB mode encryption."""
    blocks = split_blocks(plaintext, block_size)
    encrypted_blocks = []
    current_iv = iv

    for block in blocks:
        # Encrypt the IV (feedback value)
        encrypted_iv = cipher.encrypt(current_iv)
        # XOR the plaintext block with the encrypted IV
        encrypted_block = xor_bytes(block, encrypted_iv[:len(block)])
        encrypted_blocks.append(encrypted_block)
        # Update the feedback value
        current_iv = encrypted_iv

    return b''.join(encrypted_blocks)

def ofb_decrypt(ciphertext, key, iv, block_size, cipher):
    """Custom OFB mode decryption."""
    # Decryption in OFB mode is the same as encryption
    return ofb_encrypt(ciphertext, key, iv, block_size, cipher)


