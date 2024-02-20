from Crypto.Cipher import SERPENT
from Crypto.Random import get_random_bytes

def generate_key():
    return get_random_bytes(32)  # 256-bit key for Serpent

def encrypt_file(key, filename, encrypted_filename):
    cipher = SERPENT.new(key)
    with open(filename, 'rb') as f:
        data = f.read()
    # Pad the data to be a multiple of 16 bytes (Serpent block size)
    data_padded = data + bytes([16 - len(data) % 16] * (16 - len(data) % 16))
    encrypted_data = cipher.encrypt(data_padded)
    with open(encrypted_filename, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(key, encrypted_filename, decrypted_filename):
    cipher = SERPENT.new(key)
    with open(encrypted_filename, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(decrypted_filename, 'wb') as f:
        f.write(decrypted_data)

# Example usage
if __name__ == "__main__":
    key = generate_key()
    encrypt_file(key, 'plaintext.txt', 'encrypted_serpent.txt')
    decrypt_file(key, 'encrypted_serpent.txt', 'decrypted_serpent.txt')
    print("Encryption and decryption using Serpent completed.")
