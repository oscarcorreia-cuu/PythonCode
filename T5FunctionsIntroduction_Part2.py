
# Function with default parameter value
def sumNumbers(num1, num2, num3, num4=10):
    print(num1 + num2 + num3 + num4)

# sumNumbers(10,20,30)
# sumNumbers(10,20,30,50)
# sumNumbers(20,30,num3=40, num4=20) 
# sumNumbers(20,30, num4=20, num3=40) 

# def sumNumbers8(num1, num2, num3, num5, num6, num7, num8, num4=10):
#     print(num1 + num2 + num3 + num4)
#     print(num5 + num6 + num7 + num8)

# sumNumbers8(10,20,30,40,50,60,70,90)

# sumNumbers(num4=20, 20,30,  num3=40) 

# def display_info(*rags):
#     # print(rags)
#     print("\n")
#     total = 0
#     for item in rags:
#         print(item)
#         total = total + item
#     print("Total:", total)

# display_info(10)
# display_info(10, 20)
# display_info(10, 20, 30)
# display_info(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# display_info(10, 20, "a")

def display_info1(**kwargs):
    print("\n")
    print(kwargs)
    total = 0
    for key in kwargs:
        print(f"{key} : {kwargs[key]}")
        total = total + int(kwargs[key])
    print("Total:", total)

display_info1(a=10)
display_info1(a=10, b=20)
display_info1(Andrew=10, Jane=20)

def display_info2(**kwargs):
    print("\n")
    print(kwargs)
    total = 1
    for key in kwargs:
        print(f"{key} : {kwargs[key]}")
        total = total * int(kwargs[key])
    print("Total:", total)

display_info2(a=10)
display_info2(a=10, b=20)
display_info2(Andrew=10, Jane=20)