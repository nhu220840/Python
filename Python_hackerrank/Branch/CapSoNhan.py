num1, num2, num3, num4 = map(int, input().split())

q = num2 // num1

if q * num2 == num3 and q * num3 == num4:
    print("YES")
else: print("NO")