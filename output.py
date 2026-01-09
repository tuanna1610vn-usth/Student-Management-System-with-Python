from domains.Student import Student

def showStudent(student : Student):
    print(student)

def showAllStudents(students):
    for s in students.values():
        print(s)