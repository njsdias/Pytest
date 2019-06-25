from tinydb import TinyDB, Query
import datafuncs as dfn

"""
Exercise Part 3
Now, write a function test_divvy_corrupt(), that lets us compare the two CSV files and automatically finds out which
row has corrupted data. You will need to import the functions previously written.
"""
def test_divvy_corrupt():
    hash_true = dfn.hash_data('data/Divvy_Stations_2013.csv')
    hash_corr = dfn.hash_data('data/Divvy_Stations_2013_corrupt.csv')

    for i in range(len(hash_true)):
        true = hash_true.loc[i, 'hash']
        corr = hash_corr.loc[i, 'hash']

        assert true == corr, print(f"Row {i} has a problem.")


def test_divvy_filehash():
    db = TinyDB('data_integrity/hashes.db')
    filename = f'data/Divvy_Stations_2013.csv'
    filehash = dfn.hash_file(filename)
    Rec = Query()
    latest_record = db.search(Rec.filename == filename)[-1]
    assert latest_record['hash'] == filehash
