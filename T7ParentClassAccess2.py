# Method Extension Example: When a subclass needs to extend but not completely replace the behavior of a method in the parent class.
class Pie:
    def bake(self):
        print("Baking the pie at 350 degrees for 45 minutes.")

class FruitPie(Pie):
    def bake(self):
        super().bake()  # Calls the bake method from the parent class
        print("Letting the pie cool and adding a sugar glaze.")

apple_pie = FruitPie()
apple_pie.bake()
# Output:
# Baking the pie at 350 degrees for 45 minutes.
# Letting the pie cool and adding a sugar glaze.