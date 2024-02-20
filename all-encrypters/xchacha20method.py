from Crypto.Cipher import ChaCha20_Poly1305
from Crypto.Random import get_random_bytes

def generate_key():
    return get_random_bytes(32)  # 256-bit key for XChaCha20

def generate_nonce():
    return get_random_bytes(24)  # 192-bit nonce for XChaCha20

def save_key(key, filename):
    with open(filename, 'wb') as f:
        f.write(key)

def load_key(filename):
    with open(filename, 'rb') as f:
        return f.read()

def encrypt_file(key, filename, encrypted_filename):
    nonce = generate_nonce()
    cipher = ChaCha20_Poly1305.new(key=key, nonce=nonce)
    with open(filename, 'rb') as f:
        data = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(data)
    with open(encrypted_filename, 'wb') as f:
        f.write(nonce + ciphertext + tag)

def decrypt_file(key, encrypted_filename, decrypted_filename):
    with open(encrypted_filename, 'rb') as f:
        nonce = f.read(24)
        ciphertext_with_tag = f.read()
    cipher = ChaCha20_Poly1305.new(key=key, nonce=nonce)
    decrypted_data = cipher.decrypt_and_verify(ciphertext_with_tag[:-16], ciphertext_with_tag[-16:])
    with open(decrypted_filename, 'wb') as f:
        f.write(decrypted_data)

# Example usage
if __name__ == "__main__":
    key = generate_key()
    save_key(key, 'xchacha20_key.bin')
    
    encrypt_file(key, 'plaintext.txt', 'encrypted_xchacha20.txt')
    
    decrypted_filename = 'decrypted_xchacha20.txt'
    decrypt_file(key, 'encrypted_xchacha20.txt', decrypted_filename)
    print(f"Decrypted file '{decrypted_filename}' created.")
