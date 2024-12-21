# **kwargs         = allows you to pass multiple keyword-args 
# {dictionary}     * unpacking operator

def typeof(**kwargs):
    print(type(kwargs))

def print_address(**kwargs):
    for key in kwargs.keys():
        print(key)

    print()
    for value in kwargs.values():
        print(value)
    print()

    for key, value in kwargs.items():
        print(f"{key}: {value}")


typeof( street = "123 Fake St.",
        apartment = "100",
        city = "Detroit",
        state = "MI",
        zip = "54321")

print_address(street = "123 Fake St.",
              apartment = "100",
              city = "Detroit",
              state = "MI",
              zip = "54321")