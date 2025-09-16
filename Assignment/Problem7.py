a, b, c = map(int, input("Please enter 3 positive integers a, b, c: ").split())
max = a
if b > max:
    print(b, "is the largest")
elif c > max:
    print(c, "is the largest")
else:
    print(max, "is the largest")
#print("The largest number out of those 3 numbers is:", max(a, b, c))