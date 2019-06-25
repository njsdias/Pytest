# Pytest to ML

This repo was builded following the seminar occured in 2017 in Portland: Best Testing Practices for Data Science PyCon 2017.

Please watch the [video](https://www.youtube.com/watch?v=yACtdj1_IxE) to understand the importance and the basic procedure in doing test in your ML code.

- 0-Intro: Here we can see how we can test simple functions regarding with the type of the variable (np.array), the value that is returned by a function, check the values limits of a function ([0,1]) 

- 1-Test_ML: Here you can see how write tests to check a schema of a dataframe. We need have two files: data.csv and schema.yml and compare the name of columns amoung the csv file and the yml file. 

- 2-Test_ML: Here is an update of the previous exercise. Beside to check the schemas we can check in which columns we have missing values. If you know some columns have values in range [0,1] here we see how to check this statement.

- 2-Bonus: Here you used the hypoteses package to generate data that will used in the test functions. 

- 3-Bonus: Here we see how you can detect if a file was modified or not using the hash code of the file. More than that, we can generate a little DB to store the name, datetime,hashcode of the files and compare it with the actual hash code.


Advices:

- First : Build your tests inside of a file test_name.py

- Second : Build your functions inside a file datafuncs.py


- Notes:

    - Check the lines that are not tested yet (pip install pytest-cov):

            pytest --cov-report term-missing --cov

check the  [output test file](https://github.com/njsdias/Pytest/blob/master/Pytest_ML/0-Intro/3-output-bonus.txt)


- To know more about the **assert** statement consult the [site](https://www.programiz.com/python-programming/assert-statement). 

    - Key Points to Remember
    
        - Assertions are the condition or boolean expression which are always supposed to be true in the code.
        
        - Assert statement takes an expression and optional message.
        
        - Assert statement is used to check types, values of argument and the output of the function.
        
        - Assert statement is used as debugging tool as it halts the program at the point where an error occurs.

- The **[hypothesis](https://hypothesis.readthedocs.io/en/latest/data.html)** package (pip install hyphotesis) is usefull to generate data and it is used in our tests. And example can be seen in the [2-bonus folder](https://github.com/njsdias/Pytest/tree/master/Pytest_ML/2-bonus)

- The **data checks or schema checks**  are all about making sure that the data columns that you want to have are all present, and that they have the expected data types. This consists in two files
    
    - The first file is the actual data matrix.
    
    - The second file should be a metadata specification file, minimally containing the name of the CSV file it describes, and the list of columns present.
    
 Why the duplication? The list of columns is basically an implicit contract between your data provider and you, and provides a verifiable way of describing the data matrix's columns. The process can be seen in **[2-test_ML folder](https://github.com/njsdias/Pytest/tree/master/Pytest_ML/2-test_ML)**.
    


- The **file integrity** is used to answer the question: _"Has the file changed since the last time you used it?"_ To answer this question is used a **hash code**. The hash code is generated when we pass a file to the function that generate this code. Properties of hashes & hashlib functions:

    - The first property of hashes is that of the same "thing" should yield the same hash value.
    
    - Similar-looking but different strings will yield different hashes.
    
    - Using a different hashing algorithm will yield a different hash.
    
    - Number and Strings cannot be hashed
    
   The **[3-bonus folder](https://github.com/njsdias/Pytest/tree/master/Pytest_ML/3-bonus)** we can see the entire process of this.
    
    
