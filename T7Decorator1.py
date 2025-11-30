# This code illustrates the use of property decorators in Python.
# The "Pie" class shows encapsulation through getter and setter methods using the @property decorator. 
# This allows controlled access to attributes like crust_type, size, and fruit_type, preventing direct modification and ensuring the values meet specific conditions.
# The example demonstrates data encapsulation by using private attributes (with a preceding underscore) and defining public properties for controlled access, thus maintaining the integrity of the object's state.

class Pie:
    def __init__(self, crust_type, size):
        self._crust_type = crust_type
        self._size = size

    @property
    def crust_type(self):
        return self._crust_type

    @crust_type.setter
    def crust_type(self, value):
        if not value:
            raise ValueError("Crust type cannot be empty!")
        self._crust_type = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value not in ['small', 'medium', 'large']:
            raise ValueError("Size must be 'small', 'medium', or 'large'")
        self._size = value

class FruitPie(Pie):
    def __init__(self, crust_type, size, fruit_type):
        super().__init__(crust_type, size)
        self._fruit_type = fruit_type

    @property
    def fruit_type(self):
        return self._fruit_type

    @fruit_type.setter
    def fruit_type(self, value):
        if not value:
            raise ValueError("Fruit type cannot be empty!")
        self._fruit_type = value

# Create an instance the pie
fruit_pie = FruitPie('buttery', 'medium', 'apple')

# Print the details of each pie
print(f"Fruit Pie: {fruit_pie.size} size with {fruit_pie.crust_type} crust and {fruit_pie.fruit_type} filling.")

# Set the pie type to pineapple
fruit_pie.fruit_type = 'pineapple'
print(f"Fruit Pie: {fruit_pie.size} size with {fruit_pie.crust_type} crust and {fruit_pie.fruit_type} filling.")

# Error handling
# fruit_pie.fruit_type = ''
# print(f"Fruit Pie: {fruit_pie.size} size with {fruit_pie.crust_type} crust and {fruit_pie.fruit_type} filling.")