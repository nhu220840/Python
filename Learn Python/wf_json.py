# json: các giá trị trong file được lưu dưới dạng key: value

import json

employees = {
    "name": "Nhu",
    "age": 20,
    "job": "student"
}

file_path = "./Learn python/output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employees, file, indent=4) # indent=... là khoảng cách văn bản dc viết lùi vào từ lề 
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")