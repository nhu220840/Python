import csv

file_path = "./Learn python/output.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
            # print(line[0])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read that file")