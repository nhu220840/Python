n, a, b = map(int, input().split())

if a * 2 <= b:
    print(n * a)
else:
    if n % 2 == 0: print(n // 2 * b)
    else: print(n // 2 * b + a)