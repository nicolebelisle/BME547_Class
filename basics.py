# basics
x= input("Enter a Letter")
# print("You entered {}".format(x))
# print("This is a line of code.")
# print(x)
# print(16.4)
if x == "a":
    a = 1
    b = 2
    c = a + b
    print("{} + {} = {}".format(a,b,c))
elif x == "s":
    a = 20
    b = -3
    c = a-b
    print("{} - {} = {}".format(a,b,c))
elif x == "h":
    a = 5
    b = 4
    c = a * b
    print("{} * {} = {}".format(a,b,c))
else:
    print("The {} command is not recognized.".format(x))
print("Done")
