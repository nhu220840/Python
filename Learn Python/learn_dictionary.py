#dictionary: a collection of {key:value} pairs
#            ordered and changeable. NO duplicates

capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
print(capitals.get("USA"))

if capitals.get("Russia"):
    print("That capital exists")
else:
    print("That capital does not exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Detroit"})
capitals.pop("China") #pop the item corresponding to the key
capitals.popitem() #pop the last element
# capitals.clear()
print(capitals)

keys = capitals.keys()
print(keys)

values = capitals.values()
for value in capitals.values():
    print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")