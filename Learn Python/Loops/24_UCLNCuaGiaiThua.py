num1, num2 = map(int, input().split())

minimumNumber = min(num1, num2)

gcd = 1

for i in range(1, minimumNumber + 1):
    gcd *= i

print(gcd)