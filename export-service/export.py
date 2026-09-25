
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

def export_data():
    key = AESGCM.generate_key(bit_length=256)
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, b"data", None)
    return ct

# Entrypoint
def handle_request(req):
    if req.path == "/export":
        return export_data()
