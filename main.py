from domains.MarkManagement import MarkManagement
from input import inputStudent
from output import showStudent, showAllStudents

system = MarkManagement()
student = inputStudent()
system.addStudent(student)

showStudent(student)