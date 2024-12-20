num = int(input())

arr = list(map(int, input().split()))

count_even = 0; count_odd = 0
sum_even = 0; sum_odd = 0

for item in arr:
    if item % 2 == 0:
        count_even += 1
        sum_even += item
    else:
        count_odd += 1
        sum_odd += item
    
print(count_even, count_odd, sum_even, sum_odd, sep = "\n")
    
