def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char_code = ord(char) + shift
            if char.islower():
                encrypted_text += chr((shifted_char_code - ord('a')) % 26 + ord('a'))
            else:
                encrypted_text += chr((shifted_char_code - ord('A')) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted_char_code = ord(char) - shift
            if char.islower():
                decrypted_text += chr((shifted_char_code - ord('a')) % 26 + ord('a'))
            else:
                decrypted_text += chr((shifted_char_code - ord('A')) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

while True:
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_text = caesar_encrypt(text, shift)
        print("Encrypted text: ", encrypted_text)
    elif choice == '2':
        encrypted_text = input("Enter the encrypted text to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_text = caesar_decrypt(encrypted_text, shift)
        print("Decrypted text: ", decrypted_text)
    elif choice == '3':
        break
    else:
        print("Invalid Choice! Please try again.")
