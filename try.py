"""
try:
    block of code that can cause error
except:
     #code that runs if error happens
"""
try:
    num1=int(input("enter a number"))
    print(10/num1)
except:
    print("you cannot divide a number by zero")
#another example
try:
    print(x)
except NameError:
    print("The variable is not defined")


