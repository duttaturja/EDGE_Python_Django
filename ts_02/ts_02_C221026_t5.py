number = input("Enter a number: ") #takes input from user
number = int(number) #makes sure the variable is in integer
i = 1 #declares iterator with base value 1
while i < 11: #loop will stop after the i is equal to 11
    
    if i%3==0: #checks whether the iteration can be divided by 3 or not
        i+=1 #iterator increament
        continue #skips the iteration because we dont need multiplications of 3
    else:
        print(number*i) #prints the multiplication of number and i
    
    i+=1 #iterator increament