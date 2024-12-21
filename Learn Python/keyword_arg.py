def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

if __name__ == '__main__':
    hello("Hello", title = "Mrs.", first = "Nhu", last = "Do")
    hello("Hello", first = "Nhu", last = "Do", title = "Mrs.")
    # hello(first = "Nhu", last = "Do", title = "Mrs.", "Hello") incorrect positional args

    

