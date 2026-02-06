#if statement
"""
if-statement specifies a block of code to be executed if condition is true
if condition:
         block of code to be executed if condition is true
"""
x=5
if x<10:
    print(f"{x} is less than 10")
    """ if...else
    if condition:
               block of code to be executed is true
else:
    block of code to be executed if condition is false              
    """
    #a program that checks if a user is eligible to vote
    age=12
if age>=18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
     #a program that asks the user for age and checks if they can drive
user_age=int(input("enter your age"))
if user_age>=18:
    print("you can drive")
else:
    print("you cannot drive")
        #a program that asks user for a number and checks if
        #the number is even or odd. hintevennumber%2==0
num=int(input("enter a number to check if even or odd"))
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
if num1>num2:
        print(f"{num1} is greater than {num2}")
else:
        print(f"{num2} is less than {num1}")
        num1=int(input("enter the first number"))
        num2=int(input("enter the second number"))
if num1>num2:
            print("the greater number is",num1)
else:
            print("the greater number is",num2)
        #a program that asks user two numbers and prints greater number