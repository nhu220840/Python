# Ex3: find the strongest neighbour. Given an array of N positive integers.
# The task is to find the maximum for every adjacent pair in the array.
data3 = [4, 5, 6, 7, 3, 9, 11, 2, 10]

max_of_adjacent_pairs = []  # List to store the maximums

for i in range(len(data3) - 1):
    pair_max = max(data3[i], data3[i+1])  # Compare the current and next element
    max_of_adjacent_pairs.append(pair_max)

print(max_of_adjacent_pairs) # Print the list of max
