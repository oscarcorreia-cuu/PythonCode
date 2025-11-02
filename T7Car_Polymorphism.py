# This code demonstrates several key aspects of polymorphism:

# Each car type inherits from the base Car class but implements its own versions of start_engine() and accelerate()
# The test_drive() function works with any type of car (polymorphic behavior)
# Each car type has unique characteristics:

# Regular car: Standard acceleration and engine start
# Electric car: Silent start, faster acceleration, and battery management
# Sports car: Aggressive engine sound and fastest acceleration

# When you run this code, you'll see how each car type behaves differently despite being called through the same interface

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
        self.engine_started = False
    
    def start_engine(self):
        self.engine_started = True
        return f"{self.year} {self.make} {self.model}'s engine is starting..."
    
    def accelerate(self):
        if not self.engine_started:
            return "Please start the engine first!"
        self.speed += 10
        return f"Accelerating to {self.speed} mph"
    
    def brake(self):
        if self.speed == 0:
            return "Car is already stopped!"
        self.speed = max(0, self.speed - 10)
        return f"Slowing down to {self.speed} mph"

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity
        self.charge_level = 100
    
    def start_engine(self):  # Polymorphic method
        self.engine_started = True
        return f"{self.year} {self.make} {self.model} powers up silently..."
    
    def accelerate(self):  # Polymorphic method
        if not self.engine_started:
            return "Please power up first!"
        self.speed += 15  # Electric cars accelerate faster
        self.charge_level -= 2
        return f"Accelerating to {self.speed} mph (Battery: {self.charge_level}%)"

class SportsCar(Car):
    def __init__(self, make, model, year, top_speed):
        super().__init__(make, model, year)
        self.top_speed = top_speed
    
    def start_engine(self):  # Polymorphic method
        self.engine_started = True
        return f"{self.year} {self.make} {self.model}'s engine roars to life! VROOM!"
    
    def accelerate(self):  # Polymorphic method
        if not self.engine_started:
            return "Please start the engine first!"
        self.speed += 20  # Sports cars accelerate even faster
        return f"Rapidly accelerating to {self.speed} mph!"

# Example usage
def test_drive(car):
    # Demonstrates polymorphism through the test_drive function
    print(car.start_engine())
    print(car.accelerate())
    print(car.accelerate())
    print(car.brake())
    print()

# Creating different types of cars
regular_car = Car("Toyota", "Camry", 2022)
tesla = ElectricCar("Tesla", "Model 3", 2023, 82)
ferrari = SportsCar("Ferrari", "488", 2023, 205)

# Test driving each car
test_drive(regular_car)
test_drive(tesla)
test_drive(ferrari)