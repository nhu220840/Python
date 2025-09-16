# Python reading files (.txt, .json, .csv)

file_path = "./Learn python/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")