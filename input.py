from domains.MarkManagement import MarkManagement
from domains.Student import Student

def inputStudent():
    ID = input("Student ID: ")
    name = input("Student name: ")
    dob = input("Date of birth: ")
    return Student(name, ID, dob)