import random #python library to generate random integer between 1 to 100
#describing the game rules to the user below
print("Welcome to the number guessing game where you have to guess the number I am thinking in 7 attempts only.") 
number = random.randint(1,100) #taking a random number using randint fuction from random library
i = 1 #initializing the iterator
check = 0 #this is to check if the game is completed or not
while i<=7: #while loop which will repeat 7 times for 7 attempts
    print("Attempt no: ",i) #letting the user know about the attempt no
    i+=1 #iterator increment
    guess = input("Can you guess the number: ") #taking the guess of the user
    guess = int(guess) #making sure the variable is integer so we compare it with numbers in future
    if 0<guess<=100: #condition that states whether the guess of user is between 1 to 100
        if guess<number: #if the guess satisfies the upper condition and also lower than the number or not
            print("Try higher.") #letting the user know about their guess and help the user with feedback
        elif guess>number: #if the guess satisfies the upper condition and also higher than the number or not
            print("Try lower.") #letting the user know about their guess and help the user with feedback
        else: #only condition left is guess and the number is the same
            print(f"You guessed the correct number {number} in {i-1} attempts.") #letting the user know about their guess and help the user with feedback
            check = 1 #the game is completed so the value of check is changed to 1
            break #if the guess is correct the attempts will stop and end the game
    else:
        print("Invalid number!") #if the guess is not in the range of 1 to 100 letting the user know 
        continue #skip an attempt for the invalid guess

if i>7 and check==0: #checks whether 7 attempts are done and the game is not completed
    print("You dont have any more attempts left. Try again!") #if user cant guess the number between 7 attempts the game will end with this message