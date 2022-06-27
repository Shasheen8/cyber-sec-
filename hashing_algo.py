#implementing some basic hash algorithms

import hashlib

#encode text to bytes using UTF-8 encoding
message = "some text".encode()

#hash with SHA-2 (SHA-256 & SHA-512)
print ("SHA-256: ", hashlib.sha256(message).hexdigest())


print ("SHA-512: ", hashlib.sha512(message).hexdigest())