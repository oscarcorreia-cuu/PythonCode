# print("Hello World!")

def helloWorld():
    print("Hello World!")

def helloWorld1(name):
    print(f"\nHello {name}!" )
    print("How are you?")

def helloWorld2(name):
    """
    This function takes a name as input and returns a greeting message.
    """
    response = "\nHello " + name.upper()
    response = response + "\nHow are you?"
    return response

# helloWorld()

# helloWorld1("Oscar")
# helloWorld1("Akim")
# helloWorld1("Ronald")

# print(helloWorld2("MaryBright"))
# print(helloWorld2("Jeremiah"))
# print(helloWorld2("Ndlovu"))

# print(helloWorld2.__doc__)
# print(print.__doc__)    

students = ["Aarons", "Paul", "Ayere", "Mebra", "Hillary", "Ndlovu"]

for student in students:
    print(helloWorld2(student))