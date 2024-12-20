a, b, c = map(int, input().split())

if a + b <= c or a + c <= b or b + c <= a:
    print("INVALID")
else:
    if a == b == c:
        print(1)
    elif a == b or b == c or a == c:
        print(2)
    elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print(3)
    else:
        print(4)