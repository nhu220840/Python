n = int(input())
arr = list(map(int, input().split()))

max1, max2 = -1e9, -1e9

for i in range(len(arr)):
    if arr[i] > max1:
        max2 = max1
        max1 = arr[i]
    elif arr[i] > max2:
        max2 = arr[i]

print(max1, max2, sep = " ")