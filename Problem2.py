A = int(input("Please enter a positive integer: "))
print("All the even numbers from 0 to", A, "are:", end = ' ')
for i in range (0, A + 1):
    if i % 2 == 0:
        print(i, end = ' ')