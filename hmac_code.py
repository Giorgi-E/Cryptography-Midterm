import hmac
import hashlib

with open("data.txt", "rb") as f:
    message = f.read()

key = "secretkey123".encode()

h = hmac.new(key, message, hashlib.sha256)
print("HMAC:", h.hexdigest())
