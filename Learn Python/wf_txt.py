# Python writing files (.txt, .json, .csv)
# w: write file (chỉ ghi file, nếu file đã tốn tại thì sẽ ghi đè nội dung trong file cũ, nếu ko có sẽ tự tạo 1 file mới)
# x: write file (chỉ ghi file, nếu file đã tồn tại thì báo lỗi, ko thể ghi đè nội dung trong file cũ, nếu ko có sẽ tự tạo 1 file mới)
# a: append file (chỉ ghi tiếp vào file đã tồn tại)
# r: read file (chỉ đọc file)

# txt_data = "I like yoyo!"

# file_path = "./Learn python/output.txt"

# try:
#     with open(file=file_path, mode="x") as file:
#         file.write(txt_data)
#         print(f"txt file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")


employees = ["Nhu", "Cun", "Tom", "Bi"]

file_path = "./Learn python/output.txt"

try:
    with open(file=file_path, mode="w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")