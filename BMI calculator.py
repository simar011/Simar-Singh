name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
print("Hello",name + "!")
print("By the data you have entered, you are",name,",a",gender,"and",age,"years old")
print("Thank you for entering your data, please proceed forward to check your BMI")
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
BMI = weight / (height/100)**2
print(f"your BMI is {BMI}")

