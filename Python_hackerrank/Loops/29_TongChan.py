n = int(input())

arr = list(map(int, input().split()))

sum = 0

# for i in arr:
#     if i % 2 == 0:
#         sum += i

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        sum += arr[i]
    
print(sum)