class Pie:

    type = 'baked'
    def __init__(self, crust_type, size):
        self._crust_type = crust_type
        self._size = size

    # Class method decorator
    @classmethod
    def get_type(cls):
        return f"This is a {cls.type} item."

    @staticmethod
    def available_sizes():
        return ['small', 'medium', 'large']
    
# Using class methods
print(Pie.get_type())

print(Pie.available_sizes())
