# PyQt5 introduction
# GUI = Graphical User Interface

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        # set trục Ox tận 2900 là do lúc ý để 2 màn :))
        self.setGeometry(2900, 200, 700, 700)
        self.setWindowIcon(QIcon("J:/Python/Learn python/PyQt5/profile_pic.jpg"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()