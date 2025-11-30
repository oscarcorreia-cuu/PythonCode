class Pie:
    def prepare(self):
        print("Preparing a generic pie")

class FruitPie(Pie):
    def prepare(self):
        print("Preparing a fruit pie")

class MeatPie(Pie):
    def prepare(self):
        print("Preparing a meat pie")

# Example usage
generic_pie = Pie()
generic_pie.prepare()  # Output: Preparing a generic pie

apple_pie = FruitPie()
apple_pie.prepare()  # Output: Preparing a fruit pie

chicken_pie = MeatPie()
chicken_pie.prepare()  # Output: Preparing a meat pie
