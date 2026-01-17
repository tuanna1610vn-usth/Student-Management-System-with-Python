#from domains.Student import Student
import curses
#def showStudent(student : Student, stdscr):
#    stdscr

def showAllStudents(students, stdscr):
    stdscr.clear()
    stdscr.addstr(10, 30, "=== ALL STUDENTS INFORMATION ===", curses.A_BOLD | curses.A_UNDERLINE)
    i = 11
    if not students:
        stdscr.addstr(i, 30, "The student list is currently empty!")
        i += 1
    else:
        for s in students:
            stdscr.addstr(i, 30, f"{s}")
            i += 1
    stdscr.addstr(i, 30, "Press any key to continue...")
    stdscr.getch()

def showAllCourses(courses, stdscr):
    stdscr.clear()
    stdscr.addstr(10, 30, "ALL COURSES INFORMATION ===", curses.A_BOLD | curses.A_UNDERLINE)
    i = 11
    if not courses:
        stdscr.addstr(i, 30, "The course list is currently empty!")
        i += 1
    else:
        for c in courses:
            stdscr.addstr(i, 30, f"{c}")
            i += 1
    stdscr.addstr(i, 30, "Press any key to continue...")
    stdscr.getch()

def showMark(system, course_id, stdscr):
    stdscr.clear()
    stdscr.addstr(5, 30, f"=== ALL SCORE OF {course_id} ===", curses.A_BOLD | curses.A_UNDERLINE)
    i = 6
    marks = system.getMark(course_id)
    if type(marks) == str:
        stdscr.addstr(6, 30, marks)
    else:
        for m in marks:
            stdscr.addstr(i, 30, f"{m}")
            i += 1

def showStudentResult(system, student_id, stdscr):
    stdscr.clear()
    stdscr.addstr(5, 30, f"=== ACADEMIC RESULTS OF STUDENT {student_id} ===", curses.A_BOLD | curses.A_UNDERLINE)
    i = 6
    results = system.getStudentResult(student_id)
    if type(results) == str:
        stdscr.addstr(6, 30, results)
    else:
        for r in results:
            stdscr.addstr(i, 30, f"{r}")
            i += 1

def showRanking(system, stdscr):
    stdscr.clear()
    stdscr.addstr(5, 30, "=== STUDENTS RANKING BY AVERAGE GPA ===", curses.A_REVERSE)
    i = 6
    pos = 1

    rank = system.GPA_ranking()
    if not rank:
        stdscr.addstr(i, 30, "Student ranking unavailable! No information on student's GPA was recorded", curses.A_BOLD)
    else:
        for r in rank:
            name = r["Student"].getName()
            ID = r["Student"].getID()
            stdscr.addstr(i+1, 30, f"#{pos}. {name} | {ID} | {r["GPA"]}", curses.A_BOLD)
            i += 1
            pos += 1