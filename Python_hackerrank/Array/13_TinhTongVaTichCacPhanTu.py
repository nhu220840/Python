MOD = 1e9 + 7

n = int(input())
arr = list(map(int, input().split()))

sum, product = 0, 1

for i in arr:
    sum += i
    sum %= MOD

    product *= i
    product %= MOD

print(int(sum), int(product), sep = "\n")