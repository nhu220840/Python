a, b, c = map(int, input().split())

print("YES") if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and c + b > a else print("NO")