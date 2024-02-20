from Crypto.Cipher import Threefish
from Crypto.Random import get_random_bytes

def generate_key():
    return get_random_bytes(32)  # 256-bit key for Threefish

def encrypt_file(key, filename, encrypted_filename):
    cipher = Threefish.new(key)
    with open(filename, 'rb') as f:
        data = f.read()
    # Pad the data to be a multiple of 32 bytes (Threefish block size)
    data_padded = data + bytes([32 - len(data) % 32] * (32 - len(data) % 32))
    encrypted_data = cipher.encrypt(data_padded)
    with open(encrypted_filename, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(key, encrypted_filename, decrypted_filename):
    cipher = Threefish.new(key)
    with open(encrypted_filename, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(decrypted_filename, 'wb') as f:
        f.write(decrypted_data)

# Example usage
if __name__ == "__main__":
    key = generate_key()
    encrypt_file(key, 'plaintext.txt', 'encrypted_threefish.txt')
    decrypt_file(key, 'encrypted_threefish.txt', 'decrypted_threefish.txt')
    print("Encryption and decryption using Threefish completed.")
