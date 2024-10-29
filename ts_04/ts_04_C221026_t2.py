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

    #method to update age
    def update_age(self, updated_age):
        self.age = updated_age #updating the age attribute using the new parameter

#main code starts here
name1 = "Turja Dutta" #declaring the variable
age1 = 26 #declaring the variable
age1 = int(age1) #type casting
name2 = "Tanveer bhai" #declaring the variable
age2 = 89 #declaring the variable
age2 = int(age2) #type casting
person1 = Person(name1,age1) #creating an object
person2 = Person(name2,age2) #creating another object
person2.update_age(40) #updating the tanveer bhai's age to 40
person1.display_info() #showing the info of the object 1
person2.display_info() #showing the info of the object 2
#C221026 Turja Dutta