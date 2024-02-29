n = int(input())

sum = 1; factorial = 1

for i in range(1, n):
    factorial *= i
    sum += 1 / factorial

print('%.4f' % sum)