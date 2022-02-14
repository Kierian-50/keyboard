
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QLabel, QVBoxLayout


class Key(QPushButton):

    apply_caps_lock = pyqtSignal()
    apply_alt_gr = pyqtSignal()
    display_char = pyqtSignal(str)

    def __init__(self,
                 main_key_name,
                 second_key_name=None,
                 third_key_name=None,
                 width=100,
                 height=100,
                 hasLed=False,
                 parent=None):
        super(Key, self).__init__()

        # self.resize(10, 1000)
        self.setFixedWidth(width)
        self.setFixedHeight(height)
        # self.setText(key_name)

        main_layout = QVBoxLayout()
        first_line = QHBoxLayout()

        self.main_char = QLabel(main_key_name)
        self.main_char.setAlignment(Qt.AlignCenter)
        self.main_char.setObjectName("MainChar")

        first_line.addWidget(self.main_char)

        self.hasLed = hasLed
        if self.hasLed:
            self.led_icon = QLabel("○") # ○ / ⬤
            self.led_icon.setAlignment(Qt.AlignRight)
            self.led_icon.setObjectName("LedIcon")
            first_line.addWidget(self.led_icon)

        main_layout.addLayout(first_line)

        if height >= 100:
            self.second_char = QLabel(second_key_name)
            self.second_char.setAlignment(Qt.AlignCenter)
            self.second_char.setObjectName("SecondChar")

            self.third_char = QLabel(third_key_name)
            self.third_char.setAlignment(Qt.AlignCenter)
            self.third_char.setObjectName("ThirdChar")

            second_char_layout = QHBoxLayout()
            second_char_layout.addWidget(self.second_char)
            second_char_layout.addWidget(self.third_char)

            main_layout.addLayout(second_char_layout)

        self.setLayout(main_layout)
        self.setObjectName("Key")
        self.clicked.connect(self.handleClick)

    def handleClick(self):
        if self.hasLed:
            if self.led_icon.text() == "○":
                self.led_icon.setText("⬤")
            else:
                self.led_icon.setText("○")

        if self.main_char == "🔒":
            print("🔒")
            # Emit a signal to put caps lock on letter and print the second char of first line
        elif self.main_char == "alt gr":
            print("alt gr")
            # Emit a signal to put the third char of the first line
        else:
            print(self.main_char.text())
