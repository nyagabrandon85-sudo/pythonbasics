#class-is a blueprint for creating objects
#object is an instance of class
#object-attributes and methods
class Employee:
    def __init__(self,first_name,last_name, department,salary):
        self.first_name = first_name
        self.last_name= last_name
        self.salary=salary
        self.department = department
      #returns a readable string when you print object
    def __str__(self):
      return f"{self.first_name} {self.last_name} salary is {self.salary}: department {self.department}"
    def annual_salary(self):
           return f'{self.salary *12}'
    def fullname(self):
          return f'{self.first_name} {self.last_name}'
#create an object
emp1=Employee("Brandon","Nyaga","Cybersecurity",90000)
#another
emp2=Employee("Mary","Kambua","Marketing",60000)
#access the attribute value
print(emp1.first_name)
print(emp1.department)
print(emp2.first_name)
#printimg object1
print(emp1)
#calling the annual_salary()
print(emp1.annual_salary())
print(f'{emp1.first_name} salary is {emp1.annual_salary()}')
#printing object2
print(emp2)
#calling the annual salary
print(emp2.annual_salary())
print(f'{emp2.first_name} salary is {emp2.annual_salary()}')
#calling the full_name()
print(emp1.fullname())
print(emp2.fullname())

