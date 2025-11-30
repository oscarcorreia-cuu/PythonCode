class Pie:
    def __init__(self, crust_type, size):
        self.crust_type = crust_type
        self.size = size

class FruitPie(Pie):
    def __init__(self, crust_type, size, fruit_type):
        super().__init__(crust_type, size)
        self.fruit_type = fruit_type

class MeatPie(Pie):
    def __init__(self, crust_type, size, meat_type):
        super().__init__(crust_type, size)
        self.meat_type = meat_type

fruit_pie = FruitPie('buttery', 'medium', 'apple')
meat_pie = MeatPie('flaky', 'large', 'chicken')

print(f"Fruit Pie: {fruit_pie.size} size with {fruit_pie.crust_type} crust and {fruit_pie.fruit_type} filling.")
print(f"Meat Pie: {meat_pie.size} size with {meat_pie.crust_type} crust and {meat_pie.meat_type} filling.")