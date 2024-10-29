#declaring the function
def list_calc (list):
    summation = 0 #declaring the variables
    average = 0 #declaring the variables
    smallest = list[0] #declaring the variables as the first element of the list
    largest = list[0] #declaring the variables as the first element of the list
    for i in list: #for loop
        summation += i #adding the value of i in summation
        if(i>largest): #checking if i is greater than largest or not
            largest = i #if the previous condition is true largest is equal to i
        if(i<smallest): #checking if i is less than smallest or not
            smallest = i #if the previous condition is true smallest is equal to i
    
    length = len(list) #getting the length of the list
    average = summation/length #formula of average

    #showing the results
    print(f"\n1. The summation is: {summation} \n2. The smallest number is: {smallest} \n3. The largest number is : {largest} \n4. The average is: {average}")


user_list = [] #declaring the list
n = input("Enter the number of element in the list: ") #getting the user input
n = int(n) #typecasting 
for i in range(n): #taking a loop 
    element = input("Enter your elements: ") #getting elements from user 
    element = int(element) #typecasting 
    user_list.append(element) #adding the elements to the list  

list_calc(user_list) #sending the list as a parameter to the function