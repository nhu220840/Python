A = int(input("Please enter a positive integer: "))
factorial = 1
for i in range (A, 0, -1):
    factorial *= i
print("The factorial of", A, "is:", factorial)