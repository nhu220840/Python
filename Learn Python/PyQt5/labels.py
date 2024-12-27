# PyQt5 labels
# setStyleSheet(): thêm các thuộc tính như CSS

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(2900, 200, 700, 700)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 700, 200)
        # using CSS styles
        label.setStyleSheet("""color: #292929;
                            background-color: #6fdcf7;
                            font-weight: bold;
                            font-style: italic;
                            text-decoration: underline;""")
        

        label.setAlignment(Qt.AlignTop) # VERTICALLY TOP
        label.setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM
        label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER

        label.setAlignment(Qt.AlignRight) # HORIZONTALLY RIGHT
        label.setAlignment(Qt.AlignLeft) # HORIZONTALLY LEFT
        label.setAlignment(Qt.AlignHCenter) # HORIZONTALLY CENTER

        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
        label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # CENTER & CENTER
        label.setAlignment(Qt.AlignCenter) # CENTER & CENTER


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()