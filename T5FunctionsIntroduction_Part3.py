# Introduction to lamda functions
# A lambda function is a small anonymous function

def cube(x):
    print("Calculating the cube of", x)
    return x * x * x    

print(cube(3))

# A lambda function that cubes a number
cubev2 = lambda x: x * x * x

print(cubev2(3))