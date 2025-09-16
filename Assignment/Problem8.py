a, b = int(input("Please enter a positive integer a: ")), int(input("Please enter a positive integer b: "))

if a == b:
    print("Two numbers are equal")
elif a < b:
    print("There are all the number from a to b: ", end = '')
    for i in range (a, b + 1):
        print(i, end = ' ')
else:
    print("There are all the number from b to a: ", end = '')
    for i in range (a, b - 1, -1):
        print(i, end = ' ')
