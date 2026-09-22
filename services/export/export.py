
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def handle_export(data):
    # Direct algorithm call limitation
    key = os.urandom(32)
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    return encryptor.update(data.encode()) + encryptor.finalize()
