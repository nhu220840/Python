m, n = map(int, input().split())


if m % 2 == 0:
    sumOfDominoes = m // 2 * n;
else:
    sumOfDominoes = ((m - 1) // 2) * n + n // 2

print(sumOfDominoes)
