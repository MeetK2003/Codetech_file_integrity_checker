import hashlib  # This is the magic fingerprint maker!
import os       # Helps to work with files

# Function to create the hash of a file
def get_file_hash(file_path):
    # Create a fingerprint maker
    hash_func = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:  # Open file in read-binary mode
            while chunk := f.read(4096):  # Read small parts of file
                hash_func.update(chunk)   # Add parts to fingerprint
        return hash_func.hexdigest()      # Return fingerprint as string
    except FileNotFoundError:
        return None

# Save the fingerprint in a file
def save_hash(file_path, hash_value):
    with open(file_path + ".hash", "w") as f:
        f.write(hash_value)

# Load the fingerprint we saved earlier
def load_saved_hash(file_path):
    try:
        with open(file_path + ".hash", "r") as f:
            return f.read()
    except FileNotFoundError:
        return None

# Check if the file is same or changed
def check_file_integrity(file_path):
    current_hash = get_file_hash(file_path)
    saved_hash = load_saved_hash(file_path)
    
    if saved_hash is None:
        print("🆕 No saved hash found. Saving current hash...")
        save_hash(file_path, current_hash)
        print("✅ Hash saved!")
    else:
        if current_hash == saved_hash:
            print("🛡️ File is safe. No changes found.")
        else:
            print("⚠️ File has been changed!")

# 🧪 Let's test it on a file (change the path to your file)
check_file_integrity("example.txt")
