#Student data Management Program
​
class Student:
    
    def __init__(self,name,rollno,age):
        self.name = name
        self.rollno = rollno
        self.age = age
        
#function for creating student details
    def create(self,Name,Rollno,Age):
        ob = Student(Name,Rollno,Age)
        lists.append(ob)
        
#function for displaying students details        
    def display(self,ob):
        print("Name: ",ob.name)
        print("Rollno: ",ob.rollno)
        print("Age: ",ob.age)
        print("\n")
​
#creating an empty list
lists = []
​
#creating an object to access the class Student
obj = Student('', 0, 0)
​
print("Opeartions used...\n")
print("1. Add the student details \n2. List of students details \n3. Exit")
​
​
obj.create("Aanaya",1,10)
obj.create("Bob",20,9)
​
​
print("\n")
print("List of student Details...")
for i in range(lists.__len__()):
    obj.display(lists[i])
​
​
print("Data Added Successfully..")

#Command Shift
​
