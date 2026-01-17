from .Course import Course
from .Student import Student
from .Mark import Mark
import numpy as np

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
    
    def addCourse(self, course : Course):
        ID = course.getID()

        if ID in self.__courses:
            raise ValueError("Course ID already exists!")
        else:
            self.__courses[ID] = course

    def getStudent(self, ID):
        if ID in self.__students:
            return self.__students[ID]
        else:
            raise ValueError("Student ID not found!")
        
    def getCourse(self, ID):
        if ID in self.__courses:
            return self.__courses[ID]
        else:
            raise ValueError("Course ID not found!")
        
    def getAllStudents(self):
        return list(self.__students.values())
    
    def getAllCourses(self):
        return list(self.__courses.values())
    
    def getAllMarks(self):
        return self.__marks
    
    def addMark(self, student, course, score):
        if student not in self.__students.values():
            raise ValueError("Student ID not found!")
        elif course not in self.__courses.values():
            raise ValueError("Course ID not found!")
        else:
            m = Mark(student, course, None)
            m.setScore(score)
            self.__marks.append(m)
    
    def getMark(self, course_id):
        marks = []
        if course_id in self.__courses:
            for m in self.__marks:
                if course_id == m.getCourse().getID():
                    marks.append(m)
            if not marks:
                return f"No marks was input for course {m.getCourse().getName()}"
            else:
                return marks
        else:
            return f"No course with ID {course_id} was found"
        
    def getStudentResult(self, student_id):
        results = []
        if student_id in self.__students:
            for m in self.__marks:
                if student_id == m.getStudent().getID():
                    results.append(m)
            if not results:
                return f"No marks was input for student {student_id}"
            else:
                return results
        else:
            return f"No student with ID {student_id} was found"
        
    def calGPA(self, student : Student):
        # Calculate average GPA for 1 student
        results = []
        credits = []
        GPA = 0

        for m in self.__marks:
            if m.getStudent() == student:
                results.append(m.getScore())
                credits.append(m.getCourse().getCredits())
                # Linear order
        
        table = np.array([results, credits])

        for j in range(len(table[0])):
            GPA += table[0][j] * table[1][j]
        
        total_creds = np.array(credits)
        GPA /= total_creds.sum()
        return GPA
    
    def GPA_ranking(self):
        rank = []
        #GPA_list = []

        for s in self.__students.values():
            GPA = self.calGPA(s)
            #GPA_list.append(GPA)
            in4 = {}
            in4["Student"] = s
            in4["GPA"] = GPA
            rank.append(in4)
        
        #GPA_list.sort(reverse=True)
        rank.sort(key=lambda x: x["GPA"], reverse=True)
        return rank