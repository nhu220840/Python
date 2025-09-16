n = int(input())
arr = list(map(int, input().split()))

i = 0; j = len(arr) - 1

while(i < j):
    if(arr[i] != arr[j]):
        print("NO")
        quit()
    i += 1; j -= 1

print("YES")
