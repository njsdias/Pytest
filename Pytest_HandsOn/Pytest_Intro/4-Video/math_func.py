import json

class StudentDB: # Remember a class have methods. Each class needs a self argument. It is standard for python
    def __init__(self):
        self.__data = None # initiate a member variable which name "data" that is equal to None

    def connect(self, data_file):
        with open(data_file) as json_file:
            self.__data = json.load(json_file) # load db to inside the dictionary "data"

    def get_data(self, name):   # name of the student that will be searched in the dictonary "data"
        for student in self.__data['students']:
            if student['name'] == name:  # if the name is contained in the students data I just return the student info
                return student

    def close(self):   #used to
        pass




