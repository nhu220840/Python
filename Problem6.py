a, b, c = map(int, input("Please type 3 positive integers a, b, c: ").split())

if a + b <= c or a + c <= b or b + c <= a:
    print("Three integer are entered is not a triangle")
else:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print("Square triangle")
    else:
        print("Normal triangle")
