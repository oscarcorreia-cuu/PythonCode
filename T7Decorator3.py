class Pie:

    type = 'baked'
    def __init__(self, crust_type, size):
        self._crust_type = crust_type
        self._size = size

    @classmethod
    def get_type(cls):
        return f"This is a {cls.type} item."

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

def log_preparation(func):
    def wrapper(*args, **kwargs):
        print("Starting pie preparation...")
        result = func(*args, **kwargs)
        print("Pie preparation completed.")
        return result
    return wrapper

@log_preparation
def prepare_pie(pie):
    print(f"Preparing a {pie.size} {pie.fruit_type} pie with {pie.crust_type} crust.")

# Using 
print(Pie.get_type())

fruit_pie = FruitPie('flaky', 'large', 'apple')
prepare_pie(fruit_pie)