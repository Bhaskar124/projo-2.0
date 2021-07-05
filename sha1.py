import hashlib
hash_object=hashlib.sha1(b'Hello Everyone')
hex_dig=hash_object.hexdigest()
print(hex_dig)