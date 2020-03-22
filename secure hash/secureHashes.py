import hashlib

hasher_sha1 = hashlib.sha1()
hasher_sha224 = hashlib.sha3_224()
hasher_sha256 = hashlib.sha3_256()
hasher_sha384 = hashlib.sha3_384()
hasher_sha512 = hashlib.sha3_512()
hasher_md5 = hashlib.md5()

filename = 'C:/Users/rafae/PycharmProjects/checksum/ddd.txt'

with open(filename, 'rb') as open_file:
    content = open_file.read()
    hasher_sha1.update(content)
    hasher_sha224.update(content)
    hasher_sha256.update(content)
    hasher_sha384.update(content)
    hasher_sha512.update(content)
    hasher_md5.update(content)

print('Hash SHA 1:\t\t', hasher_sha1.hexdigest())
print('\nHash SHA 224:\t', hasher_sha224.hexdigest())
print('\nHash SHA 256:\t', hasher_sha256.hexdigest())
print('\nHash SHA 384:\t', hasher_sha384.hexdigest())
print('\nHash SHA 512:\t', hasher_sha512.hexdigest())
print('\nHash MD5:\t\t', hasher_md5.hexdigest())
