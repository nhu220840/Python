A = int(input("Please enter a positive integer in range 1:10. A = "))
print("The multiplication table of A:")
for i in range (0, 11):
    print(A, "x", i, "=", A * i, end = '\n')