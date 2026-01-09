class Mark():
    def __init__(self, student, course, score):
        self.__student = student
        self.__course = course
        self.__score = score

    def getStudent(self):
        return self.__student
    
    def getCourse(self):
        return self.__course
    
    def setScore(self, score):
        if 0 <= score <= 20:
            self.__score = score
        else:
            raise ValueError("Score must be between 0 and 20")
    def getScore(self):
        return self.__score
    
    def __str__(self):
        return f"Student ID: {self.__student.getID()} | Course: {self.__course.getID()} | Score: {self.getScore()}"