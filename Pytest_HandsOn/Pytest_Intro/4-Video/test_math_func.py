from math_func import StudentDB
import pytest


# To demonstrate the fixture method which is an alternative to the
# setup/teardown method
@pytest.fixture(scope='module')
def db():
    print('-------------setup-------------')
    db = StudentDB()        # just initialize StudentDB()
    db.connect('data.json') # call connect method to access the json datafile
#    return db # used without teardown
    yield db
    print('-------------teardown-------------')
    db.close()

#
## uncomment to demonstrate the setup/teardown method
#db=None   #define the global variable
#def setup_module(module):
#    print('-------------setup-------------')
#    global db
#    db = StudentDB()        # just initialize StudentDB()
#    db.connect('data.json') # call connect method to access the json datafile

#def teardown_module(module):
#    print('-------------teardown-------------')
#    db.close()

#def test_scott_data():   # used in setup/teardown solution
def test_scott_data(db):
#    db = StudentDB()        # just initialize StudentDB()
#    db.connect('data.json') # call connect method to access the json datafile
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

#def test_mark_data():   # used in setup/teardown solution
def test_mark_data(db):
#    db = StudentDB()
#    db.connect('data.json')
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'
