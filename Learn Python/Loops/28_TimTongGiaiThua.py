n = int(input())

sum = 0
product = 1

for i in range(1, n + 1):
    product *= i
    sum += product

print(sum)