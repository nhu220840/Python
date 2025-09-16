# *args     = allows you to pass multiple non-key args
# (tuple)   * unpacking operator

# def add(*args):
#     print(type(args))

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

def display_name(*args):
    for arg in args:
        print(arg, end = " ")

print(add(1, 2, 3))
print(add(1, 2, 3, 4, 5))
print("Dr.", "Spongebob", "Harold", "Squarepants", "III")
