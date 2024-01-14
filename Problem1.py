A = int(input("Please enter a positive integer: "))
print("For loop:", end = ' ')
for i in range (A, 0, -1): #A=5
    print(i, end = '')
    if(i != 1): print(',', end = '') 

print()

print("While loop:", end = ' ')
while A != 0: #A = 5
    print(A, end = '')
    if(A != 1): print(',', end = '')
    A -= 1