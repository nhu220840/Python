import tkinter as tk

class System:
    def __init__(self, root):
        self.window = root
        self.window.title("Student Management System")
        # widthxheight + x + y
        self.window.geometry("800x600+450+200")

        # frame is created in the left side of the window
        self.left_frame = tk.Frame(root, bg="#8f9494")
        self.left_frame.place(width=200, height=600)
        # create subframe in left frame
        self.list_frame = tk.Frame(self.left_frame, bg="#5df592")
        self.list_frame.place(width=300, height=100)

        # Display 'list students" button
        self.std_btn = tk.Button(
                            self.list_frame,
                            bg="#311833",
                            fg="yellow",
                            text="Student list",
                            font=("Arial", 13, "bold"),
                            relief=tk.FLAT
        )
        
        self.std_btn.grid()

        self.cs_btn = tk.Button(
                            self.list_frame,
                            bg="#332618",
                            fg="red",
                            text="Courses list",
                            font=("Arial", 13, "bold"),
                            relief=tk.FLAT
        )
        
        self.cs_btn.grid()

        # frame is created in the right side of the window
        self.right_frame = tk.Frame(root, bg="#f55d90")
        # set position for frame with x and y
        self.right_frame.place(x=root.winfo_width - self.left_frame.winfo_width, width=600, height=600)

        # Create label
        self.title_label = tk.Label(
                            self.right_frame,
                            bg="#edc1b2",
                            text="Student Management System",
                            font=("Arial", 16, "bold"),
                            padx=0,
                            pady=0
        )
        self.title_label.pack(fill=tk.X)


def main():
    root = tk.Tk()
    app = System(root)
    root.mainloop()

if __name__ == '__main__':
    main()

# Câu hỏi liên quan đến moodle exam có thể hỏi:
# Các function liên quan đến đặt vị trí của frame
# - pack(): là default (khi sử dụng pack auto đặt ra giữa, và chồng chéo theo chiều dọc), khi kéo cửa sổ window theo chiều 
# ngang thì vị trí của frame sẽ thay đổi khi kéo, auto fill full screen, 2 cái còn lại sẽ cố định
# - play(): ko khuyến khích sử dụng
# - grid(): có thể đặt vị trí cố định, khi kéo cửa sổ window thì vị trí của frame sẽ ko thay đổi
