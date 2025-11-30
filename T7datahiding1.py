class Pie:
    def __init__(self, crust_type, size):
        self.__crust_type = crust_type  # Private attribute
        self._size = size  # Protected attribute

    # Getter for private attribute
    def get_crust_type(self):
        return self.__crust_type

    # Setter for private attribute
    def set_crust_type(self, value):
        if not value:
            raise ValueError("Crust type cannot be empty!")
        self.__crust_type = value

    # Method to describe the pie
    def describe_pie(self):
        print(f"This is a {self._size} pie with {self.get_crust_type()} crust.")

# Example usage
pie = Pie('buttery', 'medium')
pie.describe_pie()  # Output: This is a medium pie with buttery crust.

# Accessing and modifying the protected attribute
pie._size = 'large'
pie.describe_pie()  # Output: This is a large pie with buttery crust.

# Using getter and setter for the private attribute
print(pie.get_crust_type())  # Output: buttery
pie.set_crust_type('flaky')
pie.describe_pie()  # Output: This is a large pie with flaky crust.

# Attempting direct access to private attribute will raise an error
# print(pie.__crust_type)  # AttributeError