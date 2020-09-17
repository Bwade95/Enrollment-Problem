from person import Person

class Teacher(Person):
    def __init__(self, firstName, lastName, dob, phoneNum, address, salary):
        super().__init__(firstName, lastName, dob, phoneNum, address)
        self.salary = salary
        self.courses = []
        self.got_raise = False

    def check_for_raise(self):
        if len(self.courses) >= 4 and not self.got_raise:
            self.salary += 20000
            self.got_raise = True

    def add_course(self, courses):
        import courses
        if not isinstance(courses, courses.Courses):
            raise NameError("Invalid course...")
        
        self.courses.append(courses)