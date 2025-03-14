# Ex1: Write a program to count positive and negative numbers in a list
data1 = [-10, -21, -4, -45, -66, 93, 11, -4, -6, 12, 11, 4]

positive_num = 0
negative_num = 0

for num in data1:
    if num > 0:
        positive_num += 1
    else:
        negative_num += 1

print(positive_num)
print(negative_num)