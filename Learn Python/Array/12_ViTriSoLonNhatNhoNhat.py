n = int(input())
arr = list(map(int, input().split()))

last_position, first_position = 0, 0
minimum_number, maximum_number = 1e9, -1e9

for i in range(len(arr)):
    if arr[i] <= minimum_number:
        minimum_number = arr[i]
        last_position = i
    
    if arr[i] > maximum_number:
        maximum_number = arr[i]
        first_position = i

print(last_position, first_position, sep = " ")