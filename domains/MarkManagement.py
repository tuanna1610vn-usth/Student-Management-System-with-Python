from .Course import Course
from .Student import Student
from .Mark import Mark

class MarkManagement():
    def __init__(self):
        self.__students = {}
        self.__courses = {}
        self.__marks = []
    
    def addStudent(self, student : Student):
        ID = student.getID()

        if ID in self.__students:
            raise ValueError("Student ID already exists!")
        else:
            self.__students[ID] = student