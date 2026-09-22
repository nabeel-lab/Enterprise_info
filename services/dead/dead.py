
import hashlib

def _deprecated_unused_hash(data):
    return hashlib.sha1(data.encode()).hexdigest()
