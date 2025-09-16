a, b, n = map(int, input().split())

flag = False

for i in range(0, n // b + 1):
    if((n - b * i) % a == 0):
        flag = True

print("YES") if flag else print("NO")