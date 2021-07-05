import hashlib
hash_object=hashlib.sha224(b'Hello Everyone')
hex_dig=hash_object.hexdigest()
print(hex_dig)