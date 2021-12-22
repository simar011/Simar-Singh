class Student:
    def __init__(self):
        self.student_name = input("\n Enter the student name: ")
        self.student_age = input("Enter the student age: ")
        self.student_gender = input("Enter the student gender: ")

    def display(self):
        print("\n Enter the student name: ",self.student_name)
        print("Enter the student age; ",self.student_age)
        print("Enter the student gender: ",self.student_gender)

class Marks:
    def __init__(self):
        self.grade = input("Enter the grade of the student: ")
        print("------- Evaluate Marks per subject --------")
        self.english = int(input("Marks in English subject: "))
        self.maths = int(input("Marks in Maths subject: "))
        self.physics = int(input("Marks in Physics subject: "))
        self.chemistry = int(input("Marks in Chemistry subject: "))
        self.computer = int(input("Marks in Computer subject: "))

    def display(self):
        self.total = self.english + self.maths + self.physics + self.chemistry + self.computer
        print("Total marks: ",self.total)

class Data(Student,Marks):
    def __init__(self):
        Student.__init__(self)
        Marks.__init__(self)

    def result(self):
        Marks.display(self)

S1 = Data()
S1.result()
S2 = Data()
S2.result()
S3 = Data()
S3.result()
S4 = Data()
S4.result()

print("You can create more objects to add objects to add more student data")
    
