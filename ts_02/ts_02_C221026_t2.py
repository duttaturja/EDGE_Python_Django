number=input() #takes input from user
number = int(number) #makes the given input integer
if number>=0 and number<=100: #checks if the number is greater than 0 or not and also not more than 100 or not
  if number>=40 and number<60: #if the given number statisfies the upper condition and also between 40 to 59
    print("Your grade is C") #returns the grade C
  elif number>=60 and number<80: #if the given number statisfies the upper condition and also between 60 to 79
    print("Your grade is B") #returns the grade B
  elif number>=80 : #if the given number statisfies the upper condition and also more than 80 
    print("Your grade is A") #returns the grade A
  else:  #if the given number statisfies the upper condition and also between 1 to 39
    print("You failed") #returns the failed the class
else: #if the given input is more than 100 or negative integer
  print("Not valid") #returns not a valid input