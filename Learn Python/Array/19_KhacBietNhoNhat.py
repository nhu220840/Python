n = int(input())
arr = list(map(int, input().split()))

minimum_distance = 1e9
for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        minimum_distance = min(minimum_distance, abs(arr[i] - arr[j]))

print(minimum_distance)