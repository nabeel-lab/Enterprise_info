
import hashlib

def hash_legacy(data):
    # MD5 usage intentionally
    return hashlib.md5(data).hexdigest()

def handle_request(req):
    if req.path == "/legacy":
        return hash_legacy(req.body)
