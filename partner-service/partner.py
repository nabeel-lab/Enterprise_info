
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

def sign_payload(data):
    # ECDSA signing
    private_key = ec.generate_private_key(ec.SECP256R1())
    signature = private_key.sign(data, ec.ECDSA(hashes.SHA256()))
    return signature

# Entrypoint
def handle_request(req):
    if req.path == "/partner":
        return sign_payload(req.body)
