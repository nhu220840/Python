import math

n = int(input())

sum = 0

for i in range(1, int(math.sqrt(n)) + 1, 1):
    if n % i == 0:
        sum += i
        if(i != n / i):
            sum += n // i

print(sum)