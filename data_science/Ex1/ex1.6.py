# Ex6:  Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

start = 2000
end = 3200

result = []

for i in range(start, end + 1):
    if i % 7 == 0 and i % 5 != 0:
        result.append(str(i))
result = ", ".join(result)
print(result)

# result6 = [str(num) for num in range(2000, 3201) if num % 7 == 0 and num % 5 != 0]
# result6 = ", ".join(result6)