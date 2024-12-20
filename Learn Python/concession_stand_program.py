menu = {"popcorn": "1.00",
        "hot dog": "2.00",
        "pretzel": "2.00",
        "candy": "1.00",
        "soda": "1.00",
        "water": "1.00"}

cart = []
total = 0

print("-----------MENU-----------")
for key, value in menu.items():
    print(f"{key:10}: ${float(value):.2f}")

print("--------------------------")

print(menu.get("popcorn"))

while True:
    food = input("Select an item (q to quit): ").lower()
    if(food == "q"):
        break
    elif menu.get(food) is not None:
        cart.append(food)
        total += float(menu.get(food))


print("--------YOUR ORDER--------")
if len(cart) == 0: print("You did not buy nothing")
for item in cart:
    print(item, end = " ")

print()
print(f"Total is: ${total:.2f}")
