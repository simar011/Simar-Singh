#Program for performing arthemetic operators
​
#Function Addition
def add(a,b):
    return a+b
​
#Function Subtraction
def sub(a,b):
    return a-b
​
#Function for Multiplication
def mul(a,b):
    return a*b
​
#Function for Division
def div(a,b):
    return a/b
​
#function for Modulous
def mod(a,b):
    return a%b
​
#function for Factorial
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)
​
num1 = int(input('Enter the 1st Number: '))
num2 = int(input('Enter the 2nd Number: '))
​
print('Addition')
print(num1 ,'+' ,num2, '=',add(num1,num2))
​
print('Subtraction')
print(num1 ,'-' ,num2, '=',sub(num1,num2))
​
print('Multiplication')
print(num1 ,'*' ,num2, '=',mul(num1,num2))
​
print('Division')
print(num1 ,'/' ,num2, '=',div(num1,num2))
​
print('Modulous')
print(num1 ,'%' ,num2, '=',mod(num1,num2))
​
num = int(input('Enter the Number :'))
print('Factorial of the number', fact(num))
