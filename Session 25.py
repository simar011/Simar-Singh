class Student:
    def __init__(self):
        self.student_name = input("\n Enter the student name: ")
        self.student_age = input("Enter the student age: ")
        self.student_gender = input("Enter the student gender: ")

    def display(self):
        print("Enter the student name: ",self.student_name)
        print("Enter the student age; ",self.student_age)
        print("Enter the student gender: ",self.student_gender)

class Marks:
    def __init__(self):
        self.grade = input("Enter the grade of the student: ")
        print("------- Evaluate Marks per subject --------")
        self.english = input("Marks in English subject: ")
        self.maths = input("Marks in Maths subject: ")
        self.physics = input("Marks in Physics subject: ")
        self.chemistry = input("Marks in Chemistry subject: ")
        self.computer = input("Marks in Computer subject: ")

    def result(self):
        print("Total Evaluated Marks: ",self.english + self.maths + self.physics + self.chemistry + self.computer)
