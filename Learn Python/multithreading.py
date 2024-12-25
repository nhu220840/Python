# multithreading =  Used to perform multiple tasks concurrently (multitasking)
#                   Good for I/O bound tasks like reading files or fetching data from APIs
#                   threading. Thread(target=my_function)

# nhiều hành động được thực hiện cùng 1 lúc

import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")
    
# nếu chỉ truyền 1 arg bắt buộc phải có dấu ',' nếu ko sẽ báo lỗi 
# bởi vì args nhận giá trị truyền vào là 1 tuples, nếu ko có dấu ',' sẽ mặc định tham số truyền vào là 1 string nên sẽ báo lỗi
# thêm dấu ',' để biến giá trị truyền vào trở thành 1 tuples
chore1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

# join có tác dụng đợi tất cả các hành động thực hiện xong mới chạy tiếp chương trình
chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")
