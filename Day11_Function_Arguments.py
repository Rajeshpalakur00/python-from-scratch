# Day11_Function_Arguments

def greet(name):
    print("Hello", name)
greet("Rajesh")

# Example using age

def Vote_Check(age):
    if age >=18:
        print("Eligible")
    else:
        print("not Eligible")
Vote_Check(25)
Vote_Check(16)

#Example Using Two Arguments

def student(name,age):
    print("Name", name)
    print("age", age)
student("rajesh", 26)

#Example Using squares

def square(number):
    print(number*number)
square(8)

# User Input + Function

def greet(name):
    print("Hello", name)
user_name = input("Enter your name:")
greet(user_name)

# User Input inside  Function
def qa(environment):
    print("Environment:", environment)
current_environment = "QA"
qa(current_environment)