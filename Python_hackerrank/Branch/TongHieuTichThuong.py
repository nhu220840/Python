a, b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
print('%.4f' % (a / b)) if b != 0 else print("INVALID")