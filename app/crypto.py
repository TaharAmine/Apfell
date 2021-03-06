from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import base64


async def hash_SHA512(data):
    digest = hashes.Hash(hashes.SHA512(), backend=default_backend())
    digest.update(str.encode(data))
    return base64.b64encode(digest.finalize())

