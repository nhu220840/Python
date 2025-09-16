n = int(input())
arr = list(map(int, input().split()))
num = int(input())

countGreaterNumber, countSmallerNumber = 0, 0

for item in arr:
    if item > num:
        countGreaterNumber += 1
    elif item < num:
        countSmallerNumber += 1

print(countSmallerNumber, countGreaterNumber, sep = "\n")