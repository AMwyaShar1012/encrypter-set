from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def save_key(key, filename):
    with open(filename, 'wb') as f:
        f.write(key)

def load_key(filename):
    with open(filename, 'rb') as f:
        return f.read()

def encrypt_file(public_key, filename, encrypted_filename):
    with open(filename, 'rb') as f:
        data = f.read()
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_data = cipher.encrypt(data)
    with open(encrypted_filename, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(private_key, encrypted_filename, decrypted_filename):
    with open(encrypted_filename, 'rb') as f:
        encrypted_data = f.read()
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(decrypted_filename, 'wb') as f:
        f.write(decrypted_data)

# Example usage
if __name__ == "__main__":
    private_key, public_key = generate_key_pair()
    save_key(private_key, 'private_key.pem')
    save_key(public_key, 'public_key.pem')
    
    encrypt_file(public_key, 'plaintext.txt', 'encrypted.txt')
    
    decrypted_filename = 'decrypted.txt'
    decrypt_file(private_key, 'encrypted.txt', decrypted_filename)
    print(f"Decrypted file '{decrypted_filename}' created.")
