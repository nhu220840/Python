n, u1, d = map(int, input().split())

un = u1 + (n - 1) * d

sum = (u1 + un) * n / 2

print(int(sum))