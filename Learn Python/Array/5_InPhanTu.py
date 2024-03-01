n = int(input())

arr = list(map(int, input().split()))

founded = False

for i in range(len(arr)):
    if i % 2 == 0 and arr[i] % 2 == 0:
        print(arr[i], end = " ")
        founded = True

if founded == False: print("NONE")

