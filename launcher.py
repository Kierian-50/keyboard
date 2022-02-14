import sys

from PyQt5.QtWidgets import QApplication

from keyboard import Keyboard

if __name__ == '__main__':
    app = QApplication(sys.argv)
    keyboard = Keyboard()
    keyboard.show()
    sys.exit(app.exec_())