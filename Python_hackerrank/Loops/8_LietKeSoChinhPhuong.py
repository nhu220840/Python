from math import *

n = int(input())

for i in range(1, int(sqrt(n)) + 1, 1):
    print(i * i, end = " ")