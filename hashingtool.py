import hashlib
import os
import argparse

SUPPORTED_ALGORITHMS = ['md5', 'sha1', 'sha256', 'sha512', 'blake2b', 'blake2s']

def generate_hash(data, algo="md5", salt=None):
    if algo not in SUPPORTED_ALGORITHMS:
        raise ValueError("Unsupported Algorithm")

    hasher = getattr(hashlib, algo)()
    
    if salt:
        data = salt + data

    hasher.update(data.encode())
    return hasher.hexdigest()

def generate_file_hash(filename, algo="md5", salt=None):
    if algo not in SUPPORTED_ALGORITHMS:
        raise ValueError("Unsupported Algorithm")

    hasher = getattr(hashlib, algo)()

    with open(filename, 'rb') as f:
        if salt:
            hasher.update(salt.encode())

        for block in iter(lambda: f.read(4096), b""):
            hasher.update(block)

    return hasher.hexdigest()

def main():
    parser = argparse.ArgumentParser(description='Advanced Hashing Tool')
    parser.add_argument('-d', '--data', help='Data to hash', default=None)
    parser.add_argument('-f', '--file', help='File to hash', default=None)
    parser.add_argument('-a', '--algorithm', help=f'Hashing Algorithm. Supported: {", ".join(SUPPORTED_ALGORITHMS)}', default='md5')
    parser.add_argument('-s', '--salt', help='Salt for hashing', default=None)
    args = parser.parse_args()

    if not args.data and not args.file:
        print("Either data (-d) or file (-f) must be provided.")
        return

    if args.data:
        print(f"Hashed data ({args.algorithm}): {generate_hash(args.data, args.algorithm, args.salt)}")
    elif args.file:
        if os.path.exists(args.file):
            print(f"File hash ({args.algorithm}): {generate_file_hash(args.file, args.algorithm, args.salt)}")
        else:
            print("File not found.")

if __name__ == "__main__":
    main()
