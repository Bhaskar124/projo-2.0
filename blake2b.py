import hashlib
hash_object=hashlib.blake2b(b'Hello Everyone')
hex_dig=hash_object.hexdigest()
print(hex_dig)