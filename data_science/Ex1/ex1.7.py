# Ex7: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

start = 1000
end = 3000
result = []

def check_even(num):
    for i in num:
        if int(i) % 2 != 0:
            return False
    return True

for i in range(start, end + 1):
    num = str(i)
    if check_even(num) == True:
        result.append(str(i))

result = ", ".join(result)
print(result)
