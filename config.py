from cryptography.fernet import Fernet

#loading encrypted key
with open("secret.key", "rb") as key_file: 
    key = key_file.read()

cipher_suite = Fernet(key) 

#decrypt my key
with open("encrypted_password", "rb") as enc_file: 
    encrypted_password = enc_file.read()

decrypted_password = cipher_suite.decrypt(encrypted_password).decode()

SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://Eliza:{decrypted_password}@localhost/weather_tracking'