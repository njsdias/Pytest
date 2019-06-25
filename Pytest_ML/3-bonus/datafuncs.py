

"""
---> Checking for changes in data file
Multiple approaches possible:

*** Check every cell against a "master" copy, assuming you have one.
    (inefficient, but good for pinpointing tampered cells)

*** Check every row against a hash of that row.
    (somewhat inefficient, but good for practice, and good for pinpointing tampered rows)

*** Check hash of a file. (most efficient way)

A good pragmatic balance is to check every row against a hash of that row; storing the hash of the row may help us
pinpoint which row may have been tampered.

================================
Exercise Part 1
Write a convenience function that hashes strings and returns the digest, and add it to datafuncs.py.
It should wrap the SHA256 algorithm.
================================
"""
from hashlib import sha256
def hash_string(string):
    """
    Convenience wrapper that returns the hash of a string.
    """
    assert isinstance(string, str), f'{string} is not a string!'
    string = string.encode('utf-8')
    return sha256(string).hexdigest()

"""
Exercise Part 2
Inside datafuncs.py, write a utility function with the signature hash_data(handle), that does the following:

    - Use pandas to open the data file as specified by the handle as the variable df.
    - Create a new DataFrame called hashes.
    - Create a new column in hashes called concat, which is each column of data from df converted to strings and
    concatenated into a contiguous string.
    - Create a new column in hashes called hash, which is the computed the hash of each row of the contiguous strings.
    - Delete the concat column from hashes.
    - Save the hashes to disk as the file hashes.csv.
================================
"""
import pandas as pd
def hash_data(handle):
    df = pd.read_csv(handle)
    hashes = pd.DataFrame()
    hashes['concat'] = df.apply(lambda x: ''.join(str(x[col]) for col in df.columns), axis=1)
    hashes['hash'] = hashes['concat'].apply(lambda x: hash_string(x))
    del hashes['concat']
    return hashes


"""
Exercise Part 3 -> Implemented in test_datafuncs.py
Now, write a function test_divvy_corrupt(), that lets us compare the two CSV files and automatically finds out which
row has corrupted data. You will need to import the functions previously written.
"""

"""

Hash of a file
It is possible to check the hash of a file. Let's add an existing implementation found online to our toolkit,
 datafuncs.py.

(All credit to StackOverflow community: http://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file)

"""
def hash_file(fname):
    filehash = sha256()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            filehash.update(chunk)
    return filehash.hexdigest()


orig = hash_file('data/Divvy_Stations_2013.csv')


corr = hash_file('data/Divvy_Stations_2013_corrupt.csv')

print(orig)
print(corr)