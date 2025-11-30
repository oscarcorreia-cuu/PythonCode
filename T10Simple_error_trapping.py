# Name:     Simple_error_trapping.py
# Function: To show simple error trapping
# Author:   Oscar Correia
# Date:     26.03.2025

print("Error trapping example!")

version = "1.0.0"

# Without error trapping
# numerator = float(input("Enter the numerator: "))
# denominator = float(input("Enter the denominator: "))
# result = numerator / denominator
# print(f"Result = {result}")

# With error trapping
try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values only.")
else:
    print(f"The result is: {result}")
finally:
    print("Thank you for using the calculator")


# file = open('This is a test.docx','r')
# # file = open("example.txt",'r')

# content = file.read()
# print(content)
# file.close()
