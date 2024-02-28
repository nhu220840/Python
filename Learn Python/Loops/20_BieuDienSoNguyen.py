n = int(input())

if n <= 1:
    print(-1)
else:
    if n % 2 == 0:
        print(n // 2)
        for i in range(1, n // 2 + 1, 1):
            print(2, end = " ")
    else:
        print((n - 1) // 2)
        for i in range(1, n // 2, 1):
            print(2, end = " ")
        print(3)