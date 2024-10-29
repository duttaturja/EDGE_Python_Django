#declaring the fuction
def sum(tuple):
    summation = 0 #declaring variables 
    for i in tuple: #using loop to access all the elements of the tuple
        summation+=i #adding the tuple elements 
    
    return summation #returning the summation

user_tuple = (1,2,3,4,5) #declaring the tuple
answer = sum(user_tuple) #sending the tuple as parameter to the function
print("The summation is: ",answer) #showing the result

user_tuple[3] = 26 #trying to assign value in tuple and seeing error