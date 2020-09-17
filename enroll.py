from courses import Courses
from student import Student
from datetime import datetime

class Enroll:
    def __init__(self, student, courses):
        if not isinstance(student, Student):
            raise NameError("Invalid Student...")
        if not isinstance(courses, Courses):
            raise NameError("Invalid course...")

        self.student = student
        self.courses = courses
        self.grade = None
        self.date = datetime.now()

    def set_grade(self, grade):
        self.grade = grade