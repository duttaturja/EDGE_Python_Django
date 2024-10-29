#declaring the factorial fuction which has a params n
def factorial (n): 
    if n == 1: #checking if n is equal to 1 or not
        return 1 #returning the value of 1 if the previous condition satisfies
    else: #if the previous condition doesnt satisfies
        return n * factorial(n-1) #returning the value of n multiplied by the factorial result of n-1

#main function start from here
number = input("Enter your number: ") #taking the number from the user
number = int(number) #making sure the given number is an integer
answer = factorial(number) #getting the factorial of the given number from the function above
print(f"The factorial result of the given number {number} is: ", answer) #showing the number to the user