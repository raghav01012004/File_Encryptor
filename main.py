from cryptography.fernet import  Fernet

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

def save_key(key,key_file):
    with open(key_file, 'wb') as f:
        f.write(key)

def load_key(key_file):
    with open(key_file,'rb') as f:
        key = f.read()
        return key
    
# Encrypt and decrypt functions
def encrypt_message(input_file,output_file,key):
    with open(input_file,'rb') as file:
        data = file.read()
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(data)
    with open(output_file,'wb') as file:
        file.write(encrypted_message)

def decrypt_message(input_file, output_file, key):
    with open(input_file,'rb') as file:
        encrypted_message = file.read()
    deciphered_message = Fernet(key).decrypt(encrypted_message)
    with open(output_file,'wb') as file:
        file.write(deciphered_message)

#usage
if __name__ == "__main__":
    key = generate_key()
    key_file = 'encryption_key.key'
    save_key(key,key_file)

    input_file = 'plain_text.txt'
    encrypted_file = 'encrypted_file.txt'
    decrypted_file = 'decrypted_file.txt'

    encrypt_message(input_file , encrypted_file , key)
    print(f"File '{input_file}' has been encrypted to '{encrypted_file}'.")

    decrypt_message(encrypted_file , decrypted_file , key)  
    print(f"File '{encrypted_file}' has been encrypted to '{decrypted_file}'.")