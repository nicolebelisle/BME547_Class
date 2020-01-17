#Calculator

def add(x,y):
    z = x + y
    print("{} + {} = {}".format(x, y, z))
    return z
def subtract(x,y):
    z = x - y
    print("{} - {} = {}".format(x, y, z))
    return z
def multiply(x,y):
    z = x * y
    print("{} * {} = {}".format(x, y, z))
    return z
def divide(x,y):
    z = x / y
    print("{} / {} = {}".format(x, y, z))
    return z

x= input("Enter a Letter")
# print("You entered {}".format(x))
# print("This is a line of code.")
# print(x)
# print(16.4)
if x == "a":
    d =add(56,73)
    if d>100:
        print("This number is too high.")
elif x == "s":
    d =subtract(1,2)
    #print("{} - {} = {}".format(a,b,c))
elif x == "h":
    a = 5
    b = 4
    c = a * b
    print("{} * {} = {}".format(a,b,c))
else:
    print("The {} command is not recognized.".format(x))
print("Done")
