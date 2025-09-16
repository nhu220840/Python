# PyQt5 images

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(2900, 200, 700, 700)

        label = QLabel(self)
        label.setGeometry(0, 0, 350, 350)

        pixmap = QPixmap("J:/Python/Learn python/PyQt5/profile_pic.jpg")
        label.setPixmap(pixmap)
        
        label.setScaledContents(True)

        # x, y, width, height:
        # - x: là trục Ox
        # - y: là trục Oy
        # - width: độ rộng của ảnh
        # - height: độ cao của ảnh
        label.setGeometry((self.width() - label.width()) // 2, # (700 - 350) / 2
                          (self.height() - label.height()) // 2, # (700 - 350) / 2
                          label.width(), # 350
                          label.height()) # 350

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()