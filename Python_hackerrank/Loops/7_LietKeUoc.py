from math import *

n = int(input())

count_divisors = 0

for i in range(1, int(sqrt(n)) + 1, 1):
    if n % i == 0:
        count_divisors += 1
        if(i != n / i):
            count_divisors += 1

print(count_divisors)
for i in range(1, n + 1, 1):
    if n % i == 0:
        print(i, end = " ")