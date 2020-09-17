from person import Person
from enroll import Enroll

class Student(Person):
    def __init__(self, firstName, lastName, dob, phoneNum, address, international=False):
        super().__init__(firstName, lastName, dob, phoneNum, address)
        self.international = international
        self.enrolled = []

    def add_enroll(self, enroll):
        if not isinstance(enroll, Enroll):
            raise NameError("Invalid Enroll")
        self.enrolled.append(enroll)

    def isPartTime(self):
        return False

    def onProbation(self):
        return len(self.enrolled) <= 3
