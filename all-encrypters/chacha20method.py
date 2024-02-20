from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes

def generate_key():
    return get_random_bytes(32)  # 256-bit key for ChaCha20

def save_key(key, filename):
    with open(filename, 'wb') as f:
        f.write(key)

def load_key(filename):
    with open(filename, 'rb') as f:
        return f.read()

def encrypt_file(key, filename, encrypted_filename):
    cipher = ChaCha20.new(key=key)
    with open(filename, 'rb') as f:
        data = f.read()
    encrypted_data = cipher.encrypt(data)
    with open(encrypted_filename, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(key, encrypted_filename, decrypted_filename):
    cipher = ChaCha20.new(key=key)
    with open(encrypted_filename, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(decrypted_filename, 'wb') as f:
        f.write(decrypted_data)

# Example usage
if __name__ == "__main__":
    key = generate_key()
    save_key(key, 'chacha20_key.bin')
    
    encrypt_file(key, 'plaintext.txt', 'encrypted_chacha20.txt')
    
    decrypted_filename = 'decrypted_chacha20.txt'
    decrypt_file(key, 'encrypted_chacha20.txt', decrypted_filename)
    print(f"Decrypted file '{decrypted_filename}' created.")
