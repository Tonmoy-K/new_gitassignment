def calculator():
    print("Hi I am empty calculator")

def multiplication(a,b):
    return a*b

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def division(a,b):
    return a/b

mult = multiplication(num1,num2)
add = addition(num1,num2)
sub = subtraction(num1,num2)
div = division(num1,num2)

num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))

print("multiplication = ",mult)
print("addition = ",add)
print("subtraction = ",sub)
print("division = ",div)


