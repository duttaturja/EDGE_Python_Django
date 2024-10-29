multi_by_3 = lambda x: x*3 #declaring the lamda function
number_list = [i for i in range(1,51)] #getting the list of 1 to 50 numbers
#loop of number list 
new_list= [(i if i%2==1 else multi_by_3(i)) for i in number_list]#using lamda funtion to get even numbers multiply by 3
print(new_list) #showing output