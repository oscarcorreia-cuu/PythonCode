def calculate1(x,y):
    return x + y

def calculate2(x,y):
    return x + y, x-y

# print(calculate2)  # Outputs: 15

# print("----")
# result1 = calculate1(5,10)
# print(result1) 
# print(result1+1) 

print("----")
result2a, result2b = calculate2(5,10)
print(result2a)  # Outputs: (15, -5)
print(result2b)

print("----")
print(result2a+1)  # Outputs: (15, -5)
print(result2b+1)


# # print(calculate2(5,10))  #