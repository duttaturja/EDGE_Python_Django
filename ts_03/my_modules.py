import math  #importing math library for pi and pow function

#declaring the fuction that converts celcius to fahrenheit
def temperature_converter (celsius):
    fahrenheit = (9/5)*celsius  #celcius to fahrenheit formula
    fahrenheit += 32 #celcius to fahrenheit formula
    return fahrenheit #returning the fahrenheit value 

#declaring the fuction that calculates area of a circle
def area_of_circle (radius):
    pi = math.pi #calling the math.pi to get the pi value from the math library
    area = pow(radius,2) #calling the pow function to square the radius
    area *= pi #area of the cirle formula
    return area #returning the area of the circles value 