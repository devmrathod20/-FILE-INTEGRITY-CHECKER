import hashlib
import json
import os

HASH_STORE = "hashes.json"

def calculate_hash(filepath):
    """Calculate SHA-256 hash of the given file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
        return None
    return sha256_hash.hexdigest()

def load_hashes():
    """Load stored hashes from JSON file."""
    if not os.path.exists(HASH_STORE):
        return {}
    with open(HASH_STORE, "r") as f:
        return json.load(f)

def save_hashes(hashes):
    """Save hashes to JSON file."""
    with open(HASH_STORE, "w") as f:
        json.dump(hashes, f, indent=4)

def add_or_update_hash(filepath):
    """Add or update hash for a file."""
    hashes = load_hashes()
    file_hash = calculate_hash(filepath)
    if file_hash:
        hashes[filepath] = file_hash
        save_hashes(hashes)
        print(f"Hash for '{filepath}' updated/stored successfully.")
    else:
        print("Hash calculation failed.")

def check_file_integrity(filepath):
    """Check if file has changed since last hash."""
    hashes = load_hashes()
    current_hash = calculate_hash(filepath)
    if current_hash is None:
        return
    stored_hash = hashes.get(filepath)
    if stored_hash:
        if current_hash == stored_hash:
            print(f"No changes detected in '{filepath}'.")
        else:
            print(f"WARNING: '{filepath}' has been modified!")
    else:
        print(f"No stored hash found for '{filepath}'. Please add it first.")

def main():
    print("=== File Integrity Checker ===")
    print("1. Add/Update file hash")
    print("2. Check file integrity")
    choice = input("Enter your choice (1/2): ")

    filepath = input("Enter the file path: ").strip()

    if choice == "1":
        add_or_update_hash(filepath)
    elif choice == "2":
        check_file_integrity(filepath)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
