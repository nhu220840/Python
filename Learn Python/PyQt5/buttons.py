# PyQt5 buttons

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(2900, 200, 700, 700)
        # khởi tạo button
        self.button = QPushButton("Click me!", self)
        # khởi tạo label
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        # set vị trí và font size cho chữ bên trong button
        self.button.setGeometry(200, 250, 300, 150)
        self.button.setStyleSheet("font-size: 30px;")

        # tín hiệu khi press button, sẽ chuyển đến hàm on_click và chạy
        self.button.clicked.connect(self.on_click)

        # set vị trí và font size cho chữ bên trong label
        self.label.setGeometry(200, 400, 300, 100)
        self.label.setStyleSheet("font-size: 50px;")

    # xử lí tín hiệu sau khi press button
    def on_click(self):
        # print("Button clicked!")
        # self.button.setText("Clicked!")

        # đổi nội dung label từ 'Hello' thành 'Good bye!!!'
        self.label.setText("Good bye!!!")
        # button ko bấm dược nữa (nghĩa là chỉ nhấn dc 1 lần)
        self.button.setDisabled(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()