n = int(input())
arr = list(map(int, input().split()))

min_distance = 1e9

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if(abs(arr[i] - arr[j]) < min_distance):
            min_distance = abs(arr[i] - arr[j])

print(min_distance)