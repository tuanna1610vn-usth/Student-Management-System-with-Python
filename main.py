from domains.MarkManagement import MarkManagement
from input import inputStudent, inputCourse, inputMark
from output import showAllStudents, showAllCourses, showMark, showStudentResult, showRanking
import curses

def main(stdscr):
    system = MarkManagement()
    loading_state = system.loadThread()

    while True:
        stdscr.clear()

        screen = """
        List of choices:
        1. Add new student(s)
        2. Show all students
        3. Add new course(s)
        4. Show all courses
        5. Add marks for student in a particular course
        6. Show all marks based on course
        7. Show academic results of a student
        8. Students ranking by GPA
        0. Exit
        """
        stdscr.addstr(10, 30, "WELCOME TO STUDENT MANAGEMENT SYSTEM", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(11, 30, "Please choose one of the following mode: ")
        stdscr.addstr(12, 30, screen)
        stdscr.addstr(0, 0, loading_state)

        stdscr.refresh()
        choice = stdscr.getkey()

        if choice == "0":
            saving_state = system.saveThread()

            stdscr.clear()
            stdscr.addstr(10, 30, "THANK YOU FOR USING STUDENT MANAGEMENT SYSTEM!", curses.A_BOLD)
            stdscr.addstr(11, 30, saving_state)
            stdscr.addstr(12, 30, "Press any key to exit...")
            stdscr.getch()
            return
        elif choice == "1":
            curses.echo()
            stdscr.clear()

            stdscr.addstr(10, 30, "=== ADD NEW STUDENT ===", curses.A_BOLD | curses.A_UNDERLINE)
            stdscr.addstr(11, 30, "Enter the number of new students: ")

            n = int(stdscr.getstr(11, 65, 5).decode("utf-8"))
            line = 11
            for i in range(n):
                stdscr.clear()
                student = inputStudent(i, line, stdscr)
                system.addStudent(student)
            
            stdscr.clear()
            stdscr.addstr(10, 30, "Students successfully added, press any key to continue...")
            stdscr.refresh()
            stdscr.getch()
        elif choice == "2":
            students = system.getAllStudents()
            showAllStudents(students, stdscr)
        elif choice == "3":
            curses.echo()
            stdscr.clear()

            stdscr.addstr(10, 30, "=== ADD NEW COURSE ===", curses.A_BOLD | curses.A_UNDERLINE)
            stdscr.addstr(11, 30, "Enter the number of new course: ")

            n = int(stdscr.getstr(11, 65, 5).decode("utf-8"))
            line = 11
            for i in range(n):
                stdscr.clear()
                course = inputCourse(i, line, stdscr)
                system.addCourse(course)
            
            stdscr.clear()
            stdscr.addstr(10, 30, "Courses successfully added, press any key to continue...")
            stdscr.refresh()
            stdscr.getch()
        elif choice == "4":
            courses = system.getAllCourses()
            showAllCourses(courses, stdscr)
        elif choice == "5":
            curses.echo()
            stdscr.clear()

            stdscr.addstr(10, 30, "=== INPUT MARKS ===", curses.A_BOLD | curses.A_UNDERLINE)
            stdscr.addstr(11, 30, "Choose a course from the current list of course: ")

            i = 1
            if not system.getAllCourses():
                stdscr.addstr(12, 30, "The list of course is currently empty!")
                stdscr.addstr(13, 30, "Press any key to continue...")
                stdscr.getch()
            else:
                for c in system.getAllCourses():
                    stdscr.addstr(11+i, 30, f"{c}", curses.A_BOLD)
                    stdscr.refresh()
                    i += 1
                stdscr.addstr(11+i, 30, "Type the ID of the course you want to choose: ")
                course_id = stdscr.getstr(11+i, 80, 20).decode("utf-8")
                course = system.getCourse(course_id)

                stdscr.addstr(12+i, 30, f"Input marks of {course.getName()} for students: ", curses.A_BOLD | curses.A_UNDERLINE)
                students = system.getAllStudents()
                marks = system.getAllMarks()

                if not marks:
                    for s in students:
                        score = inputMark(s, 13+i, stdscr)
                        i += 1
                        system.addMark(s, course, score)
                else:
                    duplicated = False
                    for s in students:
                        for m in marks:
                            if m.getStudent() == s and m.getCourse() == course:
                                duplicated = True
                        if duplicated:
                            continue
                        else:
                            score = inputMark(s, 13+i, stdscr)
                            i += 1
                            system.addMark(s, course, score)
                stdscr.addstr(29, 30, "All marks for students has been successfully added")
                stdscr.addstr(30, 30, "Press any key to continue...")
                stdscr.getch()
        elif choice == "6":
            curses.echo()
            stdscr.clear()

            stdscr.addstr(5, 30, "=== STUDENT'S RESULT BY COURSE === ", curses.A_BOLD | curses.A_UNDERLINE)
            stdscr.addstr(6, 30, "Choose a course from the current list of course: ")

            i = 1
            if not system.getAllCourses():
                stdscr.addstr(7, 30, "The list of course is currently empty!")
                stdscr.addstr(8, 30, "Press any key to continue...")
                stdscr.getch()
            else:
                for c in system.getAllCourses():
                    stdscr.addstr(6+i, 30, f"{c}", curses.A_BOLD)
                    stdscr.refresh()
                    i += 1
                stdscr.addstr(6+i, 30, "Type the ID of the course you want to choose: ")
                course_id = stdscr.getstr(6+i, 80, 20).decode("utf-8")

                showMark(system, course_id, stdscr)

                stdscr.addstr(30, 30, "Press any key to continue...")
                stdscr.getch()
        elif choice == "7":
            stdscr.clear()
            stdscr.addstr(10, 30, "=== ACADEMIC RESULT OF STUDENT ===", curses.A_BOLD | curses.A_UNDERLINE)
            stdscr.addstr(11, 30, "Enter a student ID: ")
            student_id = stdscr.getstr(11, 50, 20).decode("utf-8")

            showStudentResult(system, student_id, stdscr)

            stdscr.addstr(30, 30, "Press any key to continue...")
            stdscr.getch()
        elif choice == "8":
            showRanking(system, stdscr)

            stdscr.addstr(30, 30, "Press any key to continue...")
            stdscr.getch()
        else:
            stdscr.clear()
            stdscr.addstr(10, 40, "Error: You did NOT enter a valid key!")
            stdscr.addstr(11, 40, "Press any key to continue...")
            stdscr.refresh()
            stdscr.getch()

curses.wrapper(main)