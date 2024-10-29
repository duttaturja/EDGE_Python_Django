#defining the class
class Person:
    #initializing the class with attributes
    def __init__(self, name, age):
        self.name = name #assigning the name parameter to attribute
        self.age = age #assigning the age parameter to attribute

    #method to display details
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}") #showing results

    #method to greet
    def greet(self):
        print(f"Hello! I am {self.name}") #showing the greeting result

#main code starts here
name = input("Enter your name: ") #taking user input
age = input("Enter your age: ") #taking user input
age = int(age) #type casting

person = Person(name,age) #creating an object
person.display_info() #showing the info of the object
person.greet() #greeting using the object
