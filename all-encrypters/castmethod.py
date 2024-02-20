from Crypto.Cipher import CAST
from Crypto.Random import get_random_bytes

def generate_key():
    return get_random_bytes(16)  # 128-bit key for CAST

def encrypt_file(key, filename, encrypted_filename):
    cipher = CAST.new(key, CAST.MODE_ECB)
    with open(filename, 'rb') as f:
        data = f.read()
    # Pad the data to be a multiple of 8 bytes (CAST block size)
    data_padded = data + bytes([8 - len(data) % 8] * (8 - len(data) % 8))
    encrypted_data = cipher.encrypt(data_padded)
    with open(encrypted_filename, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(key, encrypted_filename, decrypted_filename):
    cipher = CAST.new(key, CAST.MODE_ECB)
    with open(encrypted_filename, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(decrypted_filename, 'wb') as f:
        f.write(decrypted_data)

# Example usage
if __name__ == "__main__":
    key = generate_key()
    encrypt_file(key, 'plaintext.txt', 'encrypted_cast.txt')
    decrypt_file(key, 'encrypted_cast.txt', 'decrypted_cast.txt')
    print("Encryption and decryption using CAST completed.")
