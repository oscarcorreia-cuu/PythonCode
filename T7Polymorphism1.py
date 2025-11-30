# In this example, the prepare_pie() function can handle any Pie object, demonstrating polymorphism by using a common interface for different pie types.
class Pie:
    def prepare(self):
        print("Preparing a generic pie...")

class FruitPie(Pie):
    def prepare(self):
        print("Preparing a fruit pie...")

class MeatPie(Pie):
    def prepare(self):
        print("Preparing a meat pie...")

def prepare_pie(pie):
    pie.prepare()

# Example usage
generic_pie = Pie()
apple_pie = FruitPie()
chicken_pie = MeatPie()

prepare_pie(generic_pie)  # Output: Preparing a generic pie...
prepare_pie(apple_pie)    # Output: Preparing a fruit pie...
prepare_pie(chicken_pie)  # Output: Preparing a meat pie...