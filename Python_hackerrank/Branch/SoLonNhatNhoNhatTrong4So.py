num1, num2, num3, num4 = map(int, input().split())

minimumNumber = min(num1, num2, num3, num4)
maximumNumber = max(num1, num2, num3, num4)

print(maximumNumber, minimumNumber, sep = " ")