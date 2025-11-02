# This example demonstrates several key concepts of inheritance:

# Multi-level Inheritance:
# Vehicle (base class)
#   - Car (inherits from Vehicle)
#       - ElectricCar (inherits from Car)
#       - HybridCar (inherits from Car)
#       - SportsCar (inherits from Car)

# Method Inheritance and Override:
# - Common methods inherited from parent classes
# - Methods overridden with specialized behavior
# - Use of super() to access parent class methods

# Inheritance Features Demonstrated:
# - Base class provides common attributes and methods
# - Child classes extend functionality with specialized features
# - Method overriding for customized behavior
# - super() for accessing parent class functionality

# The hierarchy shows how inheritance allows for:
# - Code reuse (common car features)
# - Specialization (specific features for each car type)
# - Polymorphic behavior (each car type can implement methods differently)

class Vehicle:
    """Base class for all vehicles"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False
        self.speed = 0
    
    def start(self):
        self.is_running = True
        return f"{self.year} {self.make} {self.model} is starting"
    
    def stop(self):
        self.is_running = False
        self.speed = 0
        return "Vehicle stopped"
    
    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    """Base class for all cars, inheriting from Vehicle"""
    def __init__(self, make, model, year, num_doors, fuel_type):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        self.fuel_type = fuel_type
        self.gear = 'P'  # P, R, N, D
    
    def shift_gear(self, gear):
        if gear in ['P', 'R', 'N', 'D']:
            self.gear = gear
            return f"Shifted to {gear}"
        return "Invalid gear selection"
    
    def get_info(self):  # Override parent method
        base_info = super().get_info()
        return f"{base_info}, {self.num_doors} doors, {self.fuel_type} fuel"

class ElectricCar(Car):
    """Electric car class, inheriting from Car"""
    def __init__(self, make, model, year, num_doors, battery_capacity):
        super().__init__(make, model, year, num_doors, "electric")
        self.battery_capacity = battery_capacity
        self.battery_level = 100
    
    def start(self):  # Override with electric-specific behavior
        self.is_running = True
        return f"{self.get_info()} powers up silently"
    
    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        return f"Battery charged to {self.battery_level}%"
    
    def get_info(self):  # Override with battery info
        base_info = super().get_info()
        return f"{base_info}, {self.battery_capacity}kWh battery"

class HybridCar(Car):
    """Hybrid car class, inheriting from Car"""
    def __init__(self, make, model, year, num_doors, battery_capacity, fuel_tank_size):
        super().__init__(make, model, year, num_doors, "hybrid")
        self.battery_capacity = battery_capacity
        self.battery_level = 100
        self.fuel_tank_size = fuel_tank_size
        self.fuel_level = 100
    
    def switch_power_mode(self, mode):
        if mode in ['electric', 'hybrid', 'gas']:
            return f"Switched to {mode} power mode"
        return "Invalid power mode"
    
    def get_info(self):  # Override with hybrid-specific info
        base_info = super().get_info()
        return f"{base_info}, {self.battery_capacity}kWh battery, {self.fuel_tank_size}L tank"

class SportsCar(Car):
    """Sports car class, inheriting from Car"""
    def __init__(self, make, model, year, num_doors, top_speed):
        super().__init__(make, model, year, num_doors, "premium")
        self.top_speed = top_speed
        self.sport_mode = False
    
    def toggle_sport_mode(self):
        self.sport_mode = not self.sport_mode
        return f"Sport mode {'activated' if self.sport_mode else 'deactivated'}"
    
    def get_info(self):  # Override with sports car info
        base_info = super().get_info()
        return f"{base_info}, {self.top_speed}mph top speed"

# Example usage demonstrating inheritance
def test_vehicles():
    # Create instances of different vehicle types
    tesla = ElectricCar("Tesla", "Model 3", 2023, 4, 82)
    prius = HybridCar("Toyota", "Prius", 2023, 4, 8.8, 43)
    porsche = SportsCar("Porsche", "911", 2023, 2, 205)
    
    # Test common inherited methods
    print("Testing inherited and specialized behaviors:\n")
    
    # Tesla demonstrations
    print("Electric Car:")
    print(tesla.get_info())
    print(tesla.start())
    print(tesla.charge(20))
    print(tesla.shift_gear('D'))
    print()
    
    # Prius demonstrations
    print("Hybrid Car:")
    print(prius.get_info())
    print(prius.start())
    print(prius.switch_power_mode('electric'))
    print(prius.shift_gear('D'))
    print()
    
    # Porsche demonstrations
    print("Sports Car:")
    print(porsche.get_info())
    print(porsche.start())
    print(porsche.toggle_sport_mode())
    print(porsche.shift_gear('D'))
    print()

if __name__ == "__main__":
    test_vehicles()