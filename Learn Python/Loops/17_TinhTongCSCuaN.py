n = int(input())

sumOfDigits = 0

while n:
    sumOfDigits += n % 10
    n //= 10

print(sumOfDigits)