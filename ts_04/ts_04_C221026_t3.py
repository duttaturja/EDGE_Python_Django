#defining the calculator of fuel effieciency
class FuelEfficiencyCalculator: 
    #method to calculate
    def calculate_fuel_efficiency(miles, fuel):
        return miles/fuel
#defining the car class
class Car:
    def __init__(self, model, fuel_efficiency):
        self.model = model #assigning the parameter to the attribute
        self.fuel_efficiency = fuel_efficiency #assigning the parameter to the attribute

    #Method for driving the car
    def drive(self):
        print(f"{self.model} is being driven.") #showing the output

#main code starts here
car = Car("Bugatti", 40) #creating the car object

car.drive() #calling the drive method

miles_driven = 400
fuel_used = 10
fuel_efficiency = FuelEfficiencyCalculator.calculate_fuel_efficiency(miles_driven, fuel_used)
print(f"Fuel Efficiency: {fuel_efficiency} miles per gallon")