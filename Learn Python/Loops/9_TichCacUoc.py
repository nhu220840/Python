from math import *

n = int(input())

product = 1

for i in range(1, int(sqrt(n)) + 1, 1):
    if n % i == 0:
        product *= i
        if(i != n / i):
            product *= n // i
print(product)