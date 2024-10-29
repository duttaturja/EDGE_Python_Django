number = 11 #declared a variable with a given value of 11
number = int(number) #makes sure the number variable is integer
for i in range (number): #for the for loop used range to generate 0 to 10 and the value will be in i
    if i==0: #if i is 0 the code will skip a loop as we need 0 to 10
        continue #skipping a rotation of the loop using continue 
    print(i) #returning the value of i 
