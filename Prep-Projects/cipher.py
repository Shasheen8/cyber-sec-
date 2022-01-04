#testing for git 
# trying to implement a basic cipher. Implementation of 256 AES Cipher
# Certain concepts to keep in mind. Galois/Counter Mode. 
# padding is important for keeping encrytpion strong and unpredictable. 

from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES