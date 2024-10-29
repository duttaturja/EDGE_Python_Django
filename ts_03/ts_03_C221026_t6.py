#declaring the function
def calculation(dict):
    average = 0 #declaring variables
    n = len(dict) #getting the length of dict
    sum = 0 #declaring variables
    lowest = min(dict.values()) #getting the minimum item of dict
    highest = max(dict.values()) #getting the maximum item of dict
    for i in dict.values(): #loop to get all the dict items
        sum += i #adding dict items to the sum
    
    average = sum/n #average formula
    print(f"Average is: {average}\nLowest is: {lowest}\nHighest is: {highest}") #showing results


student_dict = {} #declaring the dictionary
n = input("Enter the number of students: ") #getting input from user 
n = int(n) #typecasting
for i in range(n): #loop to n
    name = input("Enter students Name: ") #getting student name
    marks = input("Enter students marks: ") #getting student marks
    marks = int(marks) #typecasting
    student_dict[name] = marks #assigning both to dictionary

calculation(student_dict)
