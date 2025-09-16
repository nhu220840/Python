# Ex2: Given a list, extract all elements whose frequency is greater than k.
data2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k = 3

num_list_gt_k = []
for num in data2:
    if num > k:
        num_list_gt_k.append(num)

print(num_list_gt_k)