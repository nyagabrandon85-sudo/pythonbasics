#inheritance a child class inherits attributes and methods from parent
#super/parent class
class Animal:
    def __init__(self,name,age,):
        self.name=name
        self.age=age
    def speak(self):
        return f'Hello'
    def supermethod(self):
        return f'Hello from a method in super class'
#child/sub class
class Dog(Animal):
    def speak(self):
        return 'bark bark'
    def chrome(self):
        return f' Hello from a method in super class'
#create a dog object
mydog=Dog("Spike",9)
print(mydog.name)
#call a parent method
print(mydog.supermethod())
#overidding method
print(mydog.speak())
#calling our own method
print(mydog.chrome())
#create a cat object
class Cat(Animal):
    def speak(self):
        return 'meows meows'
mycat=Cat("Sofia",6)
print(mycat.name)
print(mycat.speak())
#call the speak method
#call me the supermethod
