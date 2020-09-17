from teacher import Teacher

class Courses:
    def  __init__(self, name, code, max_, min_, teacher):
        self.name = name
        self.code = code
        self.max = max_
        self.min = min_
        self.teachers = []
        self.enrollments = []

        if isinstance(teacher, Teacher):
            self.teachers.append(teacher)
        elif isinstance(teacher,  list):
            for entry in teacher:
                if not isinstance(entry, teacher):
                    raise NameError("Invalid teacher...")

            self.teachers = teacher
        else:
            raise NameError("Invalid teacher...")

    def add_professor(self, teacher):
        if not isinstance(teacher, Teacher):
            raise NameError("Invalid teacher...")
        self.teachers.append(teacher)

    def add_enroll(self, enroll):
        import enroll
        if not isinstance(enroll, enroll.Enroll):
            raise NameError("Invalid Enroll")
        if len(self.enrollments) == self.max:
            raise EnvironmentError("Cannot enroll, course is full...")
        self.enrollments.append(enroll)
    
    def is_cancelled(self):
        return len(self.enrollments) < self.min