#CLASS IS A BLUEPRINT OF CREATING OBJECTS
#object is an instance of a class
from list import students


class Student:
#construction
#runs automatically when an object is created
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course
    def __str__(self):
      return f"The student name is{self.name} age : {self.age} :course is {self.course}"
    def get_email(self):
      return f"{self.name}@ emobilis.ac.ke"
#create an object
#object is an instance of a class
#objectname=classname(values)
student1=Student("Brandon",19,"Cybersecurity")
print(student1)
student2=Student("Myla",19,"MIT")
print(student2)
#calling our function
print(student1.get_email())
print(student2.get_email())

