def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def split_blocks(data, block_size):
    return [data[i:i + block_size] for i in range(0, len(data), block_size)]

def combine_blocks(blocks):
    """Combines a list of blocks into a single byte sequence."""
    return b''.join(blocks)