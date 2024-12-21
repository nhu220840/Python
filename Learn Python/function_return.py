# Calculate
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Create name
def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return first_name + " " + last_name

if __name__ == '__main__':
    print(add(1, 2))
    print(subtract(1, 2))
    print(multiply(1, 2))
    print(divide(1, 2))

    full_name = create_name("nhu", "do")

    print(full_name)

