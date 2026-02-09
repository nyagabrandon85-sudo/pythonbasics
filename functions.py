#functions-perform a specific task
"""
def functionname():
  block of code

"""
def demo():
    print("Hello Good afternoon")
#calling the function
demo()
demo()

#function with parameter
def greetings(name):
    print("hello",name)
#calling the function
greetings("Brandon")
greetings("Nyaga")

#a function with multiple parameters
def studentInfo(first_name,age):
    print(f"hello {first_name} you are {age} years old")
#calling the function
studentInfo("Jayden",8)
studentInfo("Myla",17)
studentInfo("Shian",24)

#function that calculates the area of a rectangle l*w
def areaOfRectangle(l,w):
    area=l*w
    print(f"The area of the rectangle with length {l} and width {w} is {area}")
#calling the function
areaOfRectangle(10,20)
areaOfRectangle(28,56)

# function that calculates the area of the circle .a=3.14*r*r
def areaOfCircle(r):
    area=3.14*r*r
    print(f"The area of the circle with radius {r} is {area}")
#calling the function
areaOfCircle(r=10)
areaOfCircle(r=28)
