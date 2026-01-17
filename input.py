from domains.Student import Student
from domains.Course import Course
import curses

def inputStudent(i, line, stdscr):
    line += 1
    stdscr.addstr(line, 30, f"Student number #{i+1}:", curses.A_UNDERLINE)
    line += 1
    stdscr.addstr(line, 30, "Student ID: ")
    ID = stdscr.getstr(line, 50, 30).decode("utf-8")
    line += 1
    stdscr.addstr(line, 30, "Student name: ")
    name = stdscr.getstr(line, 50, 30).decode("utf-8")
    line += 1
    stdscr.addstr(line, 30, "Date of birth: ")
    dob = stdscr.getstr(line, 50, 30).decode("utf-8")
    return Student(name, ID, dob)

def inputCourse(i, line, stdscr):
    line += 1
    stdscr.addstr(line, 30, f"Course number #{i+1}:", curses.A_UNDERLINE)
    line += 1
    stdscr.addstr(line, 30, "Course ID: ")
    ID = stdscr.getstr(line, 50, 30).decode("utf-8")
    line += 1
    stdscr.addstr(line, 30, "Course name: ")
    name = stdscr.getstr(line, 50, 30).decode("utf-8")
    line += 1
    stdscr.addstr(line, 30, "Number of credits: ")
    credits = int(stdscr.getstr(line, 50, 30).decode("utf-8"))
    return Course(name, ID, credits)

def inputMark(s, line, stdscr):
    stdscr.addstr(line+1, 30, f"Student ID: {s.getID()} | Student name: {s.getName()} | Score: ")
    score = float(stdscr.getstr(line+1, 90, 2).decode("utf-8"))
    return score