import math

num = float(input())

tmp = int(num)

if num - tmp == 0.5:
    if tmp % 2 == 0:
        print(tmp + 1)
    else:
        print(round(num))
else: print(round(num))