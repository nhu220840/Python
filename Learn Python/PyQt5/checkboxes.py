# PyQt5 Checkboxes

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        # set trục Ox tận 2900 là do lúc ý để 2 màn :))
        self.setGeometry(700, 300, 700, 700)
        self.checkbox = QCheckBox("Do you like food?", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(0, 0, 500, 100)
        self.checkbox.setStyleSheet("""font-size: 30px;
                                    font-family: Arial;""")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        # print(state)
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You do not like food")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()