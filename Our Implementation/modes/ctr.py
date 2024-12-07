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

# from utils import xor_bytes, split_blocks
# from multiprocessing import Pool

# def ctr_encrypt_decrypt_serial(plaintext, key, initial_counter, block_size, cipher):
#     """Custom CTR mode encryption/decryption (serial version)."""
#     blocks = split_blocks(plaintext, block_size)
#     encrypted_blocks = []
#     counter = int.from_bytes(initial_counter, 'big')

#     for block in blocks:
#         counter_block = counter.to_bytes(block_size, 'big')
#         encrypted_counter = cipher.encrypt(counter_block)
#         encrypted_block = xor_bytes(block, encrypted_counter[:len(block)])
#         encrypted_blocks.append(encrypted_block)
#         counter += 1

#     return b''.join(encrypted_blocks)

# def ctr_encrypt_decrypt_parallel(plaintext, key, initial_counter, block_size, cipher):
#     """Custom CTR mode encryption/decryption (parallel version)."""
#     blocks = split_blocks(plaintext, block_size)
#     counter = int.from_bytes(initial_counter, 'big')

#     # Precompute counter blocks
#     counter_blocks = [counter + i for i in range(len(blocks))]

#     def encrypt_counter_block(counter_value):
#         counter_block = counter_value.to_bytes(block_size, 'big')
#         return cipher.encrypt(counter_block)

#     with Pool() as pool:
#         encrypted_counters = pool.map(encrypt_counter_block, counter_blocks)

#     # XOR plaintext with encrypted counters
#     encrypted_blocks = [xor_bytes(block, enc[:len(block)]) for block, enc in zip(blocks, encrypted_counters)]

#     return b''.join(encrypted_blocks)
