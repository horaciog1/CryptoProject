from utils import xor_bytes, split_blocks

def ctr_encrypt_decrypt(plaintext, key, initial_counter, block_size, cipher):
    blocks = split_blocks(plaintext, block_size)
    encrypted_blocks = []
    counter = int.from_bytes(initial_counter, 'big')

    for block in blocks:
        counter_block = counter.to_bytes(block_size, 'big')
        encrypted_counter = cipher.encrypt(counter_block)
        encrypted_block = xor_bytes(block, encrypted_counter[:len(block)])
        encrypted_blocks.append(encrypted_block)
        counter += 1

    return b''.join(encrypted_blocks)
