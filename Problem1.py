A = int(input("Please enter a positive integer: "))
print("For loop:", end = ' ')
for i in range (A, 0, -1):
    print(i, end = '')
    if(i != 1): print(',', end = '')

print()

print("While loop:", end = ' ')
while A != 0:
    print(A, end = '')
    if(A != 1): print(',', end = '')
    A -= 1