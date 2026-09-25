
from cryptography.hazmat.primitives.asymmetric import rsa

def verify_token(token):
    # RSA verification
    pass

# Entrypoint
def handle_request(req):
    if req.path == "/identity":
        return verify_token(req.body)
