class Car:
    def __init__(self, make, model, year, engine_type):
        # Basic vehicle information
        self.make = make
        self.model = model
        self.year = year
        self.engine_type = engine_type
        
        # Operating status and conditions
        self.engine_status = False  # Engine off
        self.speed = 0             # Current speed
        self.odometer = 0          # Miles driven
        self.fuel_level = 100      # Percentage of fuel remaining
        
    def start_engine(self):
        """Attempt to start the vehicle's engine"""
        if not self.engine_status:
            if self.fuel_level > 0:
                self.engine_status = True
                return f"{self.year} {self.make} {self.model} engine started. Ready to drive."
            return "Warning: Cannot start engine - fuel level too low."
        return "Engine is already running."

    def stop_engine(self):
        """Turn off the vehicle's engine"""
        if self.engine_status:
            if self.speed > 0:
                return "Warning: Cannot stop engine while vehicle is in motion."
            self.engine_status = False
            return f"{self.make} {self.model} engine stopped."
        return "Engine is already off."

    def accelerate(self, speed_increase):
        """Increase the vehicle's speed"""
        if not self.engine_status:
            return "Engine must be started first."
        if self.fuel_level <= 0:
            self.engine_status = False
            return "Vehicle stopped: Out of fuel."
            
        self.speed += speed_increase
        self.fuel_level -= (speed_increase * 0.1)  # Simple fuel consumption model
        return f"Accelerating to {self.speed} MPH"

    def brake(self, speed_decrease):
        """Decrease the vehicle's speed"""
        if self.speed > 0:
            self.speed = max(0, self.speed - speed_decrease)
            return f"Slowing down to {self.speed} MPH"
        return "Vehicle is already stopped"

    def get_fuel_level(self):
        """Return current fuel level"""
        return f"Fuel level: {self.fuel_level:.1f}%"

    def get_status(self):
        """Return comprehensive vehicle status"""
        return {
            "vehicle": f"{self.year} {self.make} {self.model}",
            "engine_type": self.engine_type,
            "engine_status": "Running" if self.engine_status else "Off",
            "current_speed": f"{self.speed} MPH",
            "fuel_level": f"{self.fuel_level:.1f}%",
            "odometer": f"{self.odometer} miles"
        }

# Example usage
def demonstrate_car_operations():
    # Create a car instance
    my_car = Car("BMW", "330i", 2024, "2.0L Turbo I4")
    
    # Demonstrate vehicle operations
    print("Vehicle Operations Demo:\n")
    
    # Starting the car
    print(my_car.start_engine())
    
    # Accelerating
    print(my_car.accelerate(25))
    print(my_car.get_fuel_level())
    
    # Check status
    status = my_car.get_status()
    print("\nVehicle Status:")
    for key, value in status.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    # Braking
    print(f"\n{my_car.brake(15)}")
    
    # Stop engine
    print(my_car.brake(10))  # First come to complete stop
    print(my_car.stop_engine())

# Run demonstration
if __name__ == "__main__":
    demonstrate_car_operations()