n = int(input())
arr = list(map(int, input().split()))
k = int(input())

count_pairInvalid = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == k:
            count_pairInvalid += 1

print(count_pairInvalid)