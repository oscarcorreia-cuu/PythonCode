def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!!!"
    return wrapper

@uppercase_decorator
@exclamation_decorator
def prepare_pie(pie):
    return f"Preparing a {pie.size} {pie.crust_type} pie with {pie.fruit_type} filling"

# Example usage
class FruitPie:
    def __init__(self, crust_type, size, fruit_type):
        self.crust_type = crust_type
        self.size = size
        self.fruit_type = fruit_type

apple_pie = FruitPie('buttery', 'medium', 'apple')
print(prepare_pie(apple_pie))
