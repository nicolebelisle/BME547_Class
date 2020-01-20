#Calculator

def add(a,b):
    c = a + b
    return c, "+"

def subtract(a,b):
    c = a - b
    return c, "-"

def multiply(a,b):
    c = a * b
    return c, "*"

def divide(a,b):
    c = a / b
    return c, "*"
x= input("Enter a Letter: ")
a = input("Enter First Number: ")
y = float(a)
b = input("Enter Second Number: ")
z = float(b)

if x == "a":
    answer, symbol = add(y, z)
    print("{} {} {} = {}".format(y, symbol, z, answer))

elif x == "s":
    answer, symbol = subtract(y, z)
    print("{} {} {} = {}".format(y, symbol, z, answer))
    
elif x == "m":
    answer, symbol = multiply(y, z)
    print("{} {} {} = {}".format(y, symbol, z, answer))
    
elif x == "d":
    answer, symbol = divide(y, z)
    print("{} {} {} = {}".format(y, symbol, z, answer))
    
else:
    print("The {} command is not recognized.".format(x))
print("Done")
