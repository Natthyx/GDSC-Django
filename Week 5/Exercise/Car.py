class Car:
    def __init__(self,name,model,year):
        self.name = name
        self.model = model 
        self.year = year
    def displayInfo(self):
        return self.name, self.model , self.year
    
class ElectricCar(Car):
    def __init__(self, name, model, year,battery_capacity):
        super().__init__(name, model, year)
        self.battery_capacity = battery_capacity
        self.battery_level = 0 
    def charge_battery(self, charge_percentage):
        if 0 <= charge_percentage <= 100:
            self.battery_level = min(100, self.battery_level + charge_percentage)
            print(f"Battery charged to {self.battery_level}%.")
        else:
            print("Invalid charge percentage. Please provide a value between 0 and 100.")


# Test Case
regular_car = Car(name="Mercedes-Benz", model="G-Wagon", year=2022)
print("Regular Car Info:", regular_car.displayInfo())
electric_car = ElectricCar(name="Tesla", model="Model S", year=2022, battery_capacity=75)
print("Electric Car Info:", electric_car.displayInfo())
electric_car.charge_battery(charge_percentage=80)
