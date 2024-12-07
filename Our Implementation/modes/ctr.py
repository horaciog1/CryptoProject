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

# from multiprocessing import Pool

# # Top-level function for encrypting a single counter block
# def encrypt_counter_block(counter_block, key):
#     """
#     Encrypts a single counter block using the provided key.
#     :param counter_block: A block to be encrypted.
#     :param key: Encryption key.
#     :return: Encrypted counter block.
#     """
#     from Crypto.Cipher import DES
#     cipher = DES.new(key, DES.MODE_ECB)
#     return cipher.encrypt(counter_block)

# # Helper function to generate counter blocks
# def generate_counter_blocks(iv, block_size, data_length):
#     """
#     Generates counter blocks based on the initialization vector (IV) and data length.
#     :param iv: Initialization vector.
#     :param block_size: Block size in bytes.
#     :param data_length: Total length of the plaintext.
#     :return: List of counter blocks.
#     """
#     num_blocks = (data_length + block_size - 1) // block_size
#     counter_blocks = []
#     for i in range(num_blocks):
#         counter = int.from_bytes(iv, byteorder="big") + i
#         counter_blocks.append(counter.to_bytes(block_size, byteorder="big"))
#     return counter_blocks

# # Combine encrypted counters with plaintext
# def combine_blocks(plaintext, encrypted_counters, block_size):
#     """
#     Combines plaintext with encrypted counters using XOR.
#     :param plaintext: Plaintext data.
#     :param encrypted_counters: List of encrypted counter blocks.
#     :param block_size: Block size in bytes.
#     :return: Encrypted or decrypted data.
#     """
#     result = bytearray()
#     for i, encrypted_counter in enumerate(encrypted_counters):
#         block_start = i * block_size
#         block_end = block_start + block_size
#         plaintext_block = plaintext[block_start:block_end]
#         result.extend(bytes(a ^ b for a, b in zip(plaintext_block, encrypted_counter)))
#     return result

# # CTR mode encryption/decryption (serial implementation)
# def ctr_encrypt_decrypt_serial(plaintext, key, iv, block_size, cipher):
#     """
#     Encrypts or decrypts plaintext using CTR mode in a serial manner.
#     :param plaintext: The input data (plaintext or ciphertext).
#     :param key: Encryption key.
#     :param iv: Initialization vector.
#     :param block_size: Block size in bytes.
#     :param cipher: Cipher object configured with the key.
#     :return: The processed data (encrypted or decrypted).
#     """
#     # Generate counter blocks
#     counter_blocks = generate_counter_blocks(iv, block_size, len(plaintext))

#     # Encrypt counter blocks serially
#     encrypted_counters = [cipher.encrypt(block) for block in counter_blocks]

#     # XOR plaintext with encrypted counters
#     return combine_blocks(plaintext, encrypted_counters, block_size)

# # CTR mode encryption/decryption (parallel implementation)
# def ctr_encrypt_decrypt_parallel(plaintext, key, iv, block_size, _):
#     """
#     Encrypts or decrypts plaintext using CTR mode in parallel.
#     :param plaintext: The input data (plaintext or ciphertext).
#     :param key: Encryption key.
#     :param iv: Initialization vector.
#     :param block_size: Block size in bytes.
#     :param _: Cipher object (not used in this implementation).
#     :return: The processed data (encrypted or decrypted).
#     """
#     # Generate counter blocks
#     counter_blocks = generate_counter_blocks(iv, block_size, len(plaintext))

#     # Encrypt counter blocks in parallel
#     with Pool() as pool:
#         encrypted_counters = pool.starmap(encrypt_counter_block, [(block, key) for block in counter_blocks])

#     # XOR plaintext with encrypted counters
#     return combine_blocks(plaintext, encrypted_counters, block_size)

