# PyQt5 Line Edits

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        # set trục Ox tận 2900 là do lúc ý để 2 màn :))
        self.setGeometry(700, 300, 700, 700)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self):
        # Initialize line edit
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.line_edit.setStyleSheet("""font-size: 25px;
                                        font-family: Arial;""")
        
        # Initialize button
        self.button.setGeometry(215, 10, 100, 40)
        self.button.setStyleSheet("""font-size: 25px;
                                    font-family: Arial;""")
        
        self.line_edit.setPlaceholderText("Enter your name")
        # Click button
        self.button.clicked.connect(self.submit)

    # Set up signal to press button submit
    def submit(self):
        # Receive info in line after user press submit
        text = self.line_edit.text()
        print(f"Hello {text}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()