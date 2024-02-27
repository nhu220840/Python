A = int(input("Please enter a positive integer: "))
factorial = 1
for i in range (A, 0, -1): #A = 5
    factorial *= i
    print(factorial)
print("The factorial of", A, "is:", factorial)
