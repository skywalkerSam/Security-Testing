from cryptography.fernet import Fernet


# Key Creation
key = Fernet.generate_key()
with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

# Key Showcase
with open('mykey.key', 'rb') as mykey:
    key = mykey.read()                      # Key

print(key)


# File Encryption
f = Fernet(key)

with open('grades.csv', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open ('enc_grades.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)


# File Decryption
f = Fernet(key)

with open('enc_grades.csv', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_grades.csv', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)

