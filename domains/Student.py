from .Identity import Identity

class Student(Identity):
    def __init__(self, name ,id, dob):
        super().__init__(name, id)
        self.__dob = dob
    
    def setDoB(self, dob):
        self.__dob = dob
    def getDoB(self):
        return self.__dob
    
    def __str__(self):
        return f"Name: {self._name} | ID: {self._id} | DOB: {self.__dob}"