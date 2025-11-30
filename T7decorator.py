def my_decorator(func):
    def wrapper():
        print("Something before the function runs")
        func()
        print("Something after the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius cannot be negative")

say_hello()

circle = Circle(5)
print(circle.radius)  # Access the radius like an attribute
circle.radius = 10    # Set a new value
print(circle.radius)





