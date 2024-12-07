from Crypto.Util.Padding import pad, unpad
from utils import xor_bytes, split_blocks

def cbc_encrypt(plaintext, key, iv, block_size, cipher):
    blocks = split_blocks(pad(plaintext, block_size), block_size)
    encrypted_blocks = []
    prev_cipher_block = iv

    for block in blocks:
        xor_block = xor_bytes(block, prev_cipher_block)
        encrypted_block = cipher.encrypt(xor_block)
        encrypted_blocks.append(encrypted_block)
        prev_cipher_block = encrypted_block

    return b''.join(encrypted_blocks)

def cbc_decrypt(ciphertext, key, iv, block_size, cipher):
    blocks = split_blocks(ciphertext, block_size)
    decrypted_blocks = []
    prev_cipher_block = iv

    for block in blocks:
        decrypted_block = xor_bytes(cipher.decrypt(block), prev_cipher_block)
        decrypted_blocks.append(decrypted_block)
        prev_cipher_block = block

    return unpad(b''.join(decrypted_blocks), block_size)
