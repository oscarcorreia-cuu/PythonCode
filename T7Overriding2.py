class Pie:
    def __init__(self, crust_type, size):
        self.crust_type = crust_type
        self.size = size

    def prepare(self):
        print(f"Preparing a {self.size} pie with {self.crust_type} crust.")
        self.prepare_crust()
        self.add_filling()
        self.bake()

    def prepare_crust(self):
        print("Rolling out the crust...")

    def add_filling(self):
        print("Adding generic filling...")

    def bake(self):
        print("Baking the pie...")

class FruitPie(Pie):
    def __init__(self, crust_type, size, fruit_type):
        super().__init__(crust_type, size)
        self.fruit_type = fruit_type

    def add_filling(self):
        print(f"Adding {self.fruit_type} filling...")

class MeatPie(Pie):
    def __init__(self, crust_type, size, meat_type):
        super().__init__(crust_type, size)
        self.meat_type = meat_type

    def add_filling(self):
        print(f"Adding {self.meat_type} filling...")

# Example usage
generic_pie = Pie('buttery', 'medium')
generic_pie.prepare()
# Output:
# Preparing a medium pie with buttery crust.
# Rolling out the crust...
# Adding generic filling...
# Baking the pie...
print()

apple_pie = FruitPie('flaky', 'large', 'apple')
apple_pie.prepare()
# Output:
# Preparing a large pie with flaky crust.
# Rolling out the crust...
# Adding apple filling...
# Baking the pie...
print()

chicken_pie = MeatPie('crumbly', 'small', 'chicken')
chicken_pie.prepare()
# Output:
# Preparing a small pie with crumbly crust.
# Rolling out the crust...
# Adding chicken filling...
# Baking the pie...