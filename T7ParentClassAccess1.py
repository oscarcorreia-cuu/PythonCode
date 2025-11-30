# Initialization Example: In a subclass, using super().__init__() helps ensure that the parent class's constructor is properly called, initializing its attributes.
class Pie:
    def __init__(self, crust_type, size):
        self.crust_type = crust_type
        self.size = size
        print(f"Creating a {self.size} pie with {self.crust_type} crust.")

class FruitPie(Pie):
    def __init__(self, crust_type, size, fruit_type):
        super().__init__(crust_type, size)  # Calls the parent class constructor
        self.fruit_type = fruit_type
        print(f"Adding {self.fruit_type} filling.")

apple_pie = FruitPie('flaky', 'large', 'apple')
# Output:
# Creating a large pie with flaky crust.
# Adding apple filling.