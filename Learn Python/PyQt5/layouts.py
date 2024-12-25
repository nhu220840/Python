# PyQt5 layouts

import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, 
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(2900, 200, 700, 700)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)
        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")

        # VERTICAL LAYOUTS
        # vbox = QVBoxLayout()

        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)

        # central_widget.setLayout(vbox)

        # HORIZONTAL LAYOUTS
        # hbox = QHBoxLayout()

        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)

        # central_widget.setLayout(hbox)

        # GRID LAYOUTS
        grid = QGridLayout()

        # cần thêm 2 tham số nữa là vị trí của hàng và cột (index of rows and columns start by 0)
        grid.addWidget(label1, 0, 0) # hàng 0, cột 0
        grid.addWidget(label2, 0, 1) # hàng 0, cột 1
        grid.addWidget(label3, 1, 0) # hàng 1, cột 0
        grid.addWidget(label4, 1, 1) # hàng 1, cột 1
        grid.addWidget(label5, 2, 2) # hàng 2, cột 2

        central_widget.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()