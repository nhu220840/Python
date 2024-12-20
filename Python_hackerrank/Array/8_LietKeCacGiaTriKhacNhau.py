n = int(input())
arr = list(map(int, input().split()))

print(arr[0], end = ' ')
for i in range(1, len(arr)):
    found = False
    for j in range(0, i):
        if(arr[i] == arr[j]):
            found = True
    if found == False: print(arr[i], end = " ")