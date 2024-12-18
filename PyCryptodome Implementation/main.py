import os
from des import run_des_tests
from triple_des import run_3des_tests
from aes import run_aes_tests
from blowfish import run_blowfish_tests

def generate_sample_plaintexts(sizes, directory="sample_plaintexts"):
    """Generate plaintext files of specified sizes."""
    # Ensure the directory is relative to the current script's folder
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_directory = os.path.join(script_dir, directory)

    # Create the directory if it doesn't exist
    os.makedirs(full_directory, exist_ok=True)

    paths = []
    for size in sizes:
        path = os.path.join(full_directory, f"sample_{size}MB.txt")
        with open(path, 'wb') as f:
            f.write(b'A' * size * 1024 * 1024)  # Dummy data
        paths.append(path)

    return paths

if __name__ == "__main__":
    # Define test parameters
    sample_sizes_mb = [1, 10, 100, 500, 1024]  # Sizes in MB
    sample_plaintexts = generate_sample_plaintexts(sample_sizes_mb)

    # Run tests for each algorithm
    print("Running DES tests...")
    run_des_tests(sample_plaintexts)

    print("Running 3DES tests...")
    run_3des_tests(sample_plaintexts)

    print("Running AES tests...")
    run_aes_tests(sample_plaintexts)

    print("Running Blowfish tests...")
    run_blowfish_tests(sample_plaintexts)

    print("All tests completed.")
