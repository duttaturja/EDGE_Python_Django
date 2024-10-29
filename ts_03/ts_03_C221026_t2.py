from my_modules import temperature_converter #importing the temperature converter function from my module

celcius_temperature = input("Enter your celcius temperature : ") #taking the celcius user input
celcius_temperature = float(celcius_temperature) #type casting the input as floating value
fahrenheit_temperature = temperature_converter(celcius_temperature) #converting the input to fahrenheit using imported function
fahrenheit_temperature = format(fahrenheit_temperature, ".2f") #formating the variable to set precision at 2
print("Temperature in fahrenheit is : ", fahrenheit_temperature) #showing the result of the fahrenheit temperature

from my_modules import area_of_circle #importing the area of a circle calculator function from my module
radius = input("Enter the radius of the circle : ") #taking the radius from the user
radius = float(radius) #type casting the input as floating value
area = area_of_circle(radius) #calculating the area using the imported function
area = format(area, ".2f") #formating the variable to set precision at 2
print("The area of the circle is : ", area) #showing the result 