from .Identity import Identity

class Course(Identity):
    def __init__(self, name ,id, credits):
        super().__init__(name, id)
        self.__credits = credits
    
    def setCredits(self, credits):
        self.__credits = credits
    def getCredits(self):
        return self.__credits
    
    def __str__(self):
        return f"Name: {self._name} | ID: {self._id} | Credits: {self.__credits}"