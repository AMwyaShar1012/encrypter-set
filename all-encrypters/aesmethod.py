from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, 'wb') as f:
        f.write(key)

def load_key(filename):
    with open(filename, 'rb') as f:
        return f.read()

def encrypt_file(key, filename, encrypted_filename):
    fernet = Fernet(key)
    with open(filename, 'rb') as f:
        data = f.read()
    encrypted_data = fernet.encrypt(data)
    with open(encrypted_filename, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(key, encrypted_filename, decrypted_filename):
    fernet = Fernet(key)
    with open(encrypted_filename, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(decrypted_filename, 'wb') as f:
        f.write(decrypted_data)

# Example usage
if __name__ == "__main__":
    key = generate_key()
    save_key(key, 'key.txt')
    
    encrypt_file(key, 'plaintext.txt', 'encrypted.txt')
    
    decrypted_filename = 'decrypted.txt'
    decrypt_file(load_key('key.txt'), 'encrypted.txt', decrypted_filename)
    print(f"Decrypted file '{decrypted_filename}' created.")
