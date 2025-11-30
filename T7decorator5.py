class Pie:
    def __init__(self, crust_type, size):
        self._crust_type = crust_type
        self._size = size

    # The getter method is defined using the @property decorator. It allows controlled access to the private attributes. For example:
    @property
    def crust_type(self):
        return self._crust_type

    # The setter method is defined using the @<property_name>.setter decorator. It allows controlled modification of the private attributes. For example:
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

# Example usage
pie = Pie('buttery', 'medium')
print(pie.crust_type)  # Output: buttery
pie.crust_type = 'flaky'
print(pie.crust_type)  # Output: flaky

try:
    pie.size = 'extra-large'  # This will raise a ValueError
except ValueError as e:
    print(e)  # Output: Size must be 'small', 'medium', or 'large'