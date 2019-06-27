
## Test for a DB

Here we can see an example where explained the access of a JSON file which contains
information about students. 

For this DB we develop some tests to check if the information inside of the JSON file
is equal than expected.

The first impression we can identify two main problems:

- we are repeating the same tests: so we can parametrize

- we are access to the same db several time and it consumes your computer resources

Solution for he problem:

- One solution is use the **setup** and the **teardown** method. 

- Another solution is use the **pytest fixtures**.

**Setup/Teardown** Method Solution

First we define a _setup_module_ function to turn possible access only once time to the DB and 
avoid the computer resources consume. It will be call at the beginning of your test

Second we define a _teardown_ function to close our connections or free our resources
(whatever want to do after your test). it will be called at the end of your test.

_Note_: The _setup_module_ and the _teardown_module_ will be automatically recognized by pytest 

In the output file we can see that the setup_module was run in first place, after the test and at the end the teardown was executed. 

_Remember_: Here we used pytest with the option "-s" that allow us to execute the print statements

**@pytest.fixture decorator** Solution

Here we are use the @pytest.fixture decorator with the argument *scope='module'*
which only execute the **def db()** ONCE at start the . Its avoid that we call the db than one more time. 

To close the db we comment the _return db_ and write **_yield db_** which means
execute all tests first and after that run the next code line ( _db.close()_ )