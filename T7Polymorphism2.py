# In this example, MixedPie takes a list of different Pie objects (like FruitPie and MeatPie) and prepares each of them. This demonstrates how polymorphism can be used to create more flexible and complex systems by combining multiple objects.
class Pie:
    def prepare(self):
        print("Preparing a generic pie...")

class FruitPie(Pie):
    def prepare(self):
        print("Preparing a fruit pie...")

class MeatPie(Pie):
    def prepare(self):
        print("Preparing a meat pie...")

class MixedPie(Pie):
    def __init__(self, fillings):
        self.fillings = fillings

    def prepare(self):
        print("Preparing a mixed pie with the following fillings:")
        for filling in self.fillings:
            print("About to prepare a filling: ")
            filling.prepare()

# Example usage
apple_pie = FruitPie()
chicken_pie = MeatPie()
# mixed_pie = MixedPie()
mixed_pie = MixedPie([apple_pie, chicken_pie])

mixed_pie.prepare()
# Output:
# Preparing a mixed pie with the following fillings:
# Preparing a fruit pie...
# Preparing a meat pie...