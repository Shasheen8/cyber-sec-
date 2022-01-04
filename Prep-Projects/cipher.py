#testing for git 
# trying Implementation of 256 AES Cipher
# Certain concepts to keep in mind. Galois/Counter Mode. 
# padding is important for keeping encrytpion strong and unpredictable. 

from base64 import b64encode, b64decode
import hashlib
import os 
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes


def encrypt(plain_text, password):
    #generate random salt
    salt = get_random_bytes(AES.block_size)

    #Scrypt KDF to get a private key from the password
    #nouce is a random arbitrary value each time the encryption function is used
    #n is the cost factor
    #r is the block size 
    #p is teh parallelization factor 
    #tag is used to authenticate when using AES in GCM mode 
    private_key = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)

    #create cypher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    #return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    return {
        'cipher_text': b64encode(cipher_text).decode('utf-8'),
        'salt': b64encode(salt).decode('utf-8'),
        'nouce': b64encode(cipher_config.nouce).decode('utf-8'),
        'tag': b64encode(tag).decode('utf-8')
    }

def decrypt(enc_dict, password):
    #decode dictionary entries from base64
    cipher_text = b64decode(enc_dict['cipher_text'])
    salt = b64decode(enc_dict['salt'])
    nouce = b64decode(enc_dict['nouce'])
    tag = b64decode(enc_dict['tag'])

    #Scrypt to generate private key from the password and salt
    private_key = hashlib.scrypt(password.encode(),salt=salt, n=2**14, p=1, dklen=32)

    cipher = AES.new(private_key, AES.MODE_GCM, nouce=nouce)

    #decrypt the cipher text
    decrypted = cipher.decyrpt_and_verify(cipher_text, tag)
    
    return decrypted

def main():
    password = input("Password: ")

    #encrypt the message 
    encrypted = encrypt("Type your message here",password)
    print (encrypted)

    #decrypt the message
    decrypted = decrypt(encrypted, password)
    print(bytes.decode(decrypted))

main()