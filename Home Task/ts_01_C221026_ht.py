name1 = "python"
name2 = "django"
name3 = "IIUC"
name4 = "Edge Training"
name5 = "   turja    "
age = 24
price = 17.543

#case1
full_name = name1+" "+name2
print("1. Concatinating: ", full_name) # adding two strings and a space in between
#case2
print("2. To upper: ",name1.upper()) # making the whole string in capital letters
#case3
print("3. To lower: ", name3.lower()) # making the whole string in small letters
#case4
print("4. Slicing: ",full_name[2:11]) # cutting a portion out of an string
#case5
print("5. Slicing from start: ", full_name[3:]) # cutting the string from the start
#case6
print("6. Slicing from end: ", full_name[:10]) # cutting the string from the end
#case7
print("7. Negative slicing: ", full_name[-3:-8]) # cutting the string from the back using negative index
#case8
print("8. Negative slicing from start: ", full_name[:-5]) # cutting the string from the start using negative indexes
#case9
print("9. Negative slicing from end: ", full_name[-4:]) # cutting the string from the end using negative indexes
#case10
print("10. Swapcaseing: ", name4.swapcase()) # Swaping the cases of the string
#case11
print("11. Replaceing: ", name2.replace(" ",",")) # replacing space with ,
#case12
print("12. Spliting: ", full_name.split(" ")) # splitting a big string in to two parts between the space 
#case13
print("13. Finding: ", full_name.find("d")) # finding the "d" letter in the string
#case14
print("14. Counting: ", full_name.count("o")) # Counting how many times the letter "o" occured in the string
#case15
print("15. Starts with: ", name2.startswith("d")) # starts with returns whether the string starts with given letter or not
#case16
print("16. Capitalizing: ", name3.capitalize()) # capitalizing the first letter of the string
#case17
print("17. Titling: ", full_name.title()) # titling the first letter of the each word in the string
#case18
print("18. String striping: ", name5.strip()) # strips the string and removes extra spaces 
#case19
text1 = f"I am turja and I am {age} years old" # using f string to format
print("19. Using format strings: ",text1) # without using concatenation we use int value dyanamically like react
#case 20
text2 = f"With discount this cost me around {price:.2f} dollars" # using f string to format also using 2 digits after the point(.)
print("20. Using format strings with float value: ", text2)# without using concatenation we use float value dyanamically like react
#case 21
text3 = "we can use quotes in the string like \"this\"" # to use quotes in a string we have to use \"\" this
print("21. Using the quotation in a string: ", text3) # printing the quoted string 
#case22
print("22. Casefolding: ", name3.casefold()) # using casefold to lower case the letters in the string
#case23
print("23. Is lower: ", name3.islower()) # checks whether the string is in lower case or not
#case24
print("24. Is upper: ", name1.isupper()) # checks whether the string is in upper case or not
#case25
print("25. Is digit: ", name2.isdigit()) # checks whether the string is in digints or not
#case26
print("26. Is alpha: ", full_name.isalpha()) # checks whether the string is in alphabets or not
#case27
print("27. Is alphanumeric: ", name4.isalnum()) # checks whether the string is in alphanumeric or not
#case28
print("28. Is ASCII: ", name1.isascii()) # checks whether the strings all characters are ascii characters or not
#case29
print("29. Is decimal: ", name3.isdecimal()) # checks whether the strings all characters are decimals or not
#case30
print("30. Is identifier: ", name2.isidentifier()) # checks whether the string is an identifier or not 
#case31
print("31. Is numeric: ", name4.isnumeric()) # checks whether the strings all characters are numeric or not
#case32
print("32. Is space: ", name5.isspace()) # checks whether the strings all characters are white space or not
#case33
print("33. Is title: ", name4.istitle()) # checks whether the string follow the rules of a title
#case34
print("34. Is printable: ", full_name.isprintable()) # checks whether the string is printable or not
#case35
print("35. Ends with: ", full_name.endswith("o")) # ends with with returns whether the string ends with given letter or not
#case36
print("36. Centering : ", name3.center(10,"-")) # # filling the empty spaces left in the string of size 10 using '-' both sides equally
#case37
text4 = "Hello\tWorld" # used tab in a string using \t
print("37. Expanding tabs: ", text4.expandtabs(4)) # expands the tab command by 4
#case38
print("38. Reverse finding: ", name1.rfind("y")) # finding the "y" letter from the end to the start of the string 
#case39
print("39. Converting to ASCII: ", ord("A")) # converting character "A" into its ascii value
#case40
print("40. Converting ASCII value to character: ", chr(65)) # converting ASCII value to character
#case41
print("41. Partitioning: ", name2.partition("a")) # partintioning the string into a tuple based on the separator "a"
#case42
print("42. Reverse Partitioning: ",name1.rpartition("y")) # partitioning the string in to a tuple based on the separator "y" but this time with reverse
#case 43
print("43. Palindrome Checking: ",full_name == full_name[::-1]) # checking whether tha string is palindrom or not
#case44
print("44. Repeating the string: ",name3*4) # repeating the string 4x times
#case45
print("45. Zero filling: ", name1.zfill(10)) # fills 10 characters with zero at the end
#case46
print("46. Left striping: ", name5.lstrip()) # strips the string from the left side
#case47
print("47. Right striping: ", name5.rstrip()) # strips the string from the right side
#case 48
text6 = "I am Turja and I am {} years old" # this time without using the f string
print("48. Formating the string without f string: ", text6.format(age)) # we can add int value to string using format function
#case49
print("49. Right justifying: ", name1.rjust(10,'-')) # filling the empty spaces left in the string of size 10 using '-' on the left
#case50
print("50. Left justifying: ", name2.ljust(10,'-')) # filling the empty spaces left in the string of size 10 using '-' on the right


"""
Helps were taken from:
w3schools python strings methods
chatgpt
"""