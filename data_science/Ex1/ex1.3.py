# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]

maximum_num = []

for i in range(len(data3) - 1):
    maximum_num.append(max(data3[i], data3[i + 1]))

print(maximum_num)
    
