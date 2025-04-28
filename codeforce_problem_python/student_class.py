class Student:

    def __init__(self, name, group, gpa):
        self.name = name
        self.group = group
        self.gpa = gpa

    def good_student(self):
        if self.gpa >= 4.80:
            return True
        else:
            return False
