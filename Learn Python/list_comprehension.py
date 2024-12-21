# List comprehension = A concise way to create lists in Python
#                     Compact and ez to read than traditional loops
#                     [expression for value in iterable if condition]

# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)

# print(doubles)

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z ** 2 for z in range(1, 11)]

print(doubles)
print(triples)
print(squares)


# fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]
fruits_characters = [fruit[0] for fruit in fruits]

print(fruits)
print(fruits_characters)


numbers = [1, -2, 3, -4, 5, -6, 8, 10]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num <= 0]
even_nums = [num for num in numbers if num % 2 == 0]

grades = [85, 42, 79, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(passing_grades)