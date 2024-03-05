n = int(input())
arr = list(map(int, input().split()))

if arr[0] * arr[1] < 0:
    print(arr[0], end = " ")

for i in range(1, len(arr) - 1):
    if arr[i] * arr[i - 1] < 0 or arr[i] * arr[i + 1] < 0:
        print(arr[i], end = " ")

if arr[len(arr) - 1] * arr[len(arr) - 2] < 0:
    print(arr[len(arr) - 1], end = " ")