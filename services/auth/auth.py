
import hashlib

def login(password):
    # MD5 usage for legacy auth hashing!
    return hashlib.md5(password.encode()).hexdigest()
