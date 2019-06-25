""""
----> File Integrity
With file integrity, the basic question we are answering is: "Has the file changed since the last time you used it?"

----> Hash (Browns)
File integrity can be checked by checking the "hash" of a file.

The layman definition of a hash: A fixed-length, scrambled string that uniquely identifies "a thing".

The layman definition of a hashing function: A function that transforms "a thing" into a hash.

----> hashlib
hashlib is part of the Python standard library, and it provides a library of hashing functions for hashing objects,
    strings, etc.
"""

from hashlib import sha256, md5

m = sha256()
m.update('hello'.encode('utf-8'))
m.hexdigest()
print('hash: sha256-->',m.hexdigest())

"""
---->  Properties of hashes & hashlib functions

The first property of hashes is that of the same "thing" should yield the same hash value.

Using a different hashing algorithm will yield a different hash.
"""

n = md5()
n.update('hello'.encode('utf-8'))
n.hexdigest()
print('hash: md5-->',n.hexdigest())

""" Hashing functions don't work on all objects. """
try:
    o = sha256()
    o.update(3)
except TypeError:
    print('Numbers cannot be hashed')

"""
The difference among the next two "try" is that in the first the encode-utf8 was not applied
"""

try:
    o = sha256()
    o.update('Hello world!')
except TypeError:
    print('Strings cannot be hashed without encoding.')

try:
    o = sha256()
    o.update('Hello world!'.encode('utf-8'))
    print(o.hexdigest())
except TypeError:
    print('Strings must be encoded first.')

