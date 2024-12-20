n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    found = True
    for j in range(0, i):
        if arr[i] == arr[j]:
            found = False
    
    if found == True:
        count = 1
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                count += 1

        print(arr[i], count, sep = " ")
