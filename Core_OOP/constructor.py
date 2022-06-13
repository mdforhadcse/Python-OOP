class Student:
    id = ""
    gpa = ""

    def __init__(self, id, gpa):
        self.id = id
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.id}, GPA : {self.gpa}")


rahim = Student(1602067, 3.196)
rahim.display()

karim = Student(4545, 3.544)
karim.display()
