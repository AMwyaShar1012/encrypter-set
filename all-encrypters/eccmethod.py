from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt

def generate_key_pair():
    private_key = generate_key()
    public_key = private_key.public_key
    return private_key.to_hex(), public_key.to_hex()

def save_key(key, filename):
    with open(filename, 'w') as f:
        f.write(key)

def load_key(filename):
    with open(filename, 'r') as f:
        return f.read()

def encrypt_file(public_key_hex, filename, encrypted_filename):
    with open(filename, 'rb') as f:
        data = f.read()
    encrypted_data = encrypt(public_key_hex, data)
    with open(encrypted_filename, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(private_key_hex, encrypted_filename, decrypted_filename):
    with open(encrypted_filename, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = decrypt(private_key_hex, encrypted_data)
    with open(decrypted_filename, 'wb') as f:
        f.write(decrypted_data)

# Example usage
if __name__ == "__main__":
    private_key_hex, public_key_hex = generate_key_pair()
    save_key(private_key_hex, 'private_key.txt')
    save_key(public_key_hex, 'public_key.txt')
    
    encrypt_file(public_key_hex, 'plaintext.txt', 'encrypted.txt')
    
    decrypted_filename = 'decrypted.txt'
    decrypt_file(private_key_hex, 'encrypted.txt', decrypted_filename)
    print(f"Decrypted file '{decrypted_filename}' created.")
