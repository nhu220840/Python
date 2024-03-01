n = int(input())
arr = list(map(int, input().split()))

minimumNumber = 1e9
for item in arr:
    if item < minimumNumber:
        minimumNumber = item

countMinimumNumber = 0
for item in arr:
    if item == minimumNumber:
        countMinimumNumber += 1

print(countMinimumNumber)
