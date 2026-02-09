#function with return keyword return a value

#function that adds two numbers
def addTwoNumbers(a,b):
    sum=a+b
    return sum
#calling the function and storing the returned value in a variable
result=addTwoNumbers(40,30)
print("The sum is",result)
#Way two
print(addTwoNumbers(75,25))

#function that multiplies 3 numbers
def multiplyThreeNumbers(a,b,c):
    multiply=a*b*c
    return multiply
#calling the function
result=multiplyThreeNumbers(40,30,10)
print("The multiplication is",result)

#function that checks if a number is even or odd
def evenOrOdd(c):
    if c%2==0:
        print(c,"is an even number")
    else:
        print(c,"is an odd number")
 #get user input
num=int(input("Enter a number to check if even or odd"))
#calling the function
evenOrOdd(num)

#function that finds maximum of two numbers
def maximum(a,b):
    return max(a,b)
print(maximum(10,20))
