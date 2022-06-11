class Student:
    id = ""
    gpa = ""

    def set_value(self, id, gpa):
        self.id = id
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.id}, GPA : {self.gpa}")


rahim = Student()
# print(isinstance(rahim, Student))  # for checking
# rahim.id = 1602067
# rahim.gpa = 3.196
# print(f"Roll : {rahim.id}, GPA : {rahim.gpa}") #we can did the same thing using method
rahim.set_value(1602067, 3.196)
rahim.display()

karim = Student()
# print(isinstance(karim, Student))  # for checking
karim.id = 1602050
karim.gpa = 3.46
# print(f"Roll : {karim.id}, GPA : {karim.gpa}") #we can did the same thing using method
karim.display()
