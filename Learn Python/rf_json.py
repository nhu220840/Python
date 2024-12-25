import json

file_path = "./Learn python/output.json"

try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
        print(content["name"])
        print(content["age"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")