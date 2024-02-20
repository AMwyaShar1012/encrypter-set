from Crypto.Cipher import Salsa20
from Crypto.Random import get_random_bytes

def generate_key():
    return get_random_bytes(32)  # 256-bit key for Salsa20

def encrypt_file(key, filename, encrypted_filename):
    cipher = Salsa20.new(key=key)
    with open(filename, 'rb') as f:
        data = f.read()
    encrypted_data = cipher.encrypt(data)
    with open(encrypted_filename, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(key, encrypted_filename, decrypted_filename):
    cipher = Salsa20.new(key=key)
    with open(encrypted_filename, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(decrypted_filename, 'wb') as f:
        f.write(decrypted_data)

# Example usage
if __name__ == "__main__":
    key = generate_key()
    encrypt_file(key, 'plaintext.txt', 'encrypted_salsa20.txt')
    decrypt_file(key, 'encrypted_salsa20.txt', 'decrypted_salsa20.txt')
    print("Encryption and decryption using Salsa20 completed.")

