# csv = comma separated value (những giá trị sẽ cách nhau bằng dấu phẩy)
import csv

employees = [["Name", "Age", "Job"],
             ["Nhu", 20, "Student"],
             ["Cun", 21, "AI"],
             ["Tom", 17, "Unemployed"]]

file_path = "./Learn python/output.csv"

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")