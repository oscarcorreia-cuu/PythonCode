# This example demonstrates several key principles of encapsulation:

# Data Hiding:
# - Private attributes with double underscores (__)
# - Private methods that are only used internally
# - Protection from direct external access

# Access Control:
# - Getter methods using the @property decorator
# - Setter methods with validation using the .setter decorator
# - Controlled access to internal state

# Encapsulation Benefits:
# - Data validation before setting values
# - Internal state management (like engine temperature)
# - Complex interactions handled internally (fuel consumption, mileage tracking)

# The code shows how encapsulation helps maintain the object's internal state while providing a clean, controlled interface for external code to interact with.

class Car:
    def __init__(self, make, model, year):
        # Private attributes (double underscore)
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = 0
        self.__engine_temperature = 0
        self.__fuel_level = 100
        self.__is_engine_on = False
        
    # Getter methods
    @property
    def make(self):
        return self.__make
    
    @property
    def model(self):
        return self.__model
    
    @property
    def year(self):
        return self.__year
    
    @property
    def mileage(self):
        return self.__mileage
    
    @property
    def fuel_level(self):
        return self.__fuel_level
    
    # Setter methods with validation
    @fuel_level.setter
    def fuel_level(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Fuel level must be a number")
        if value < 0:
            raise ValueError("Fuel level cannot be negative")
        if value > 100:
            raise ValueError("Fuel level cannot exceed 100%")
        self.__fuel_level = value
    
    # Private method
    def __check_engine_temperature(self):
        if self.__engine_temperature > 90:
            return "WARNING: Engine temperature too high!"
        return "Engine temperature normal"
    
    # Public methods that use encapsulated attributes
    def start_engine(self):
        if self.__fuel_level < 5:
            return "Cannot start engine: Fuel level too low"
        self.__is_engine_on = True
        self.__engine_temperature += 30
        return f"{self.__year} {self.__make} {self.__model}'s engine is now running"
    
    def stop_engine(self):
        if not self.__is_engine_on:
            return "Engine is already off"
        self.__is_engine_on = False
        self.__engine_temperature = max(0, self.__engine_temperature - 30)
        return "Engine stopped"
    
    def drive(self, distance):
        if not self.__is_engine_on:
            return "Please start the engine first"
        
        fuel_consumption = distance * 0.1  # Simple fuel consumption model
        if fuel_consumption > self.__fuel_level:
            return "Not enough fuel for this distance"
        
        self.__mileage += distance
        self.__fuel_level -= fuel_consumption
        self.__engine_temperature += 10
        
        status = f"Drove {distance} miles.\n"
        status += f"Current mileage: {self.__mileage}\n"
        status += f"Remaining fuel: {self.__fuel_level:.1f}%\n"
        status += self.__check_engine_temperature()
        
        return status

# Example usage
def main():
    my_car = Car("Toyota", "Camry", 2023)
    
    # Accessing public properties
    print(f"Car: {my_car.make} {my_car.model} {my_car.year}")
    
    # Starting and driving the car
    print(my_car.start_engine())
    print(my_car.drive(50))
    
    # Demonstrating encapsulation and validation
    try:
        my_car.fuel_level = 50  # This works
        print(f"Fuel level set to: {my_car.fuel_level}%")
        
        # my_car.fuel_level = -10  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")
    
    # This would raise an AttributeError (uncomment to test):
    # print(my_car.__fuel_level)  # Cannot access private attribute directly
    # print(my_car.__check_engine_temperature())  # Cannot access private method directly

if __name__ == "__main__":
    main()