from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget

from key import Key


class Keyboard(QWidget):

    def __init__(self):
        super().__init__()

        self.red = 255
        self.green = 0
        self.blue = 0

        main_layout = QVBoxLayout()

        main_layout.addLayout(self.create_first_line())
        main_layout.addLayout(self.create_second_line())
        main_layout.addLayout(self.create_third_line())
        main_layout.addLayout(self.create_fourth_line())
        main_layout.addLayout(self.create_fifth_line())

        self.setStyleSheet(open('./style.qss').read())
        self.setLayout(main_layout)

        self.timer = QTimer()  # set up your QTimer
        self.timer.timeout.connect(self.update_color_respiration)  # connect it to your update function
        self.timer.start(1)  # set it to timeout in 1 ms

#        Key.display_char.connect(self.handle_click)

    def create_first_line(self):
        first_line = QHBoxLayout()

        first_line.addWidget(Key(main_key_name="²", parent=self))
        first_line.addWidget(Key(main_key_name="&", second_key_name="1", parent=self))
        first_line.addWidget(Key(main_key_name="é", second_key_name="2", third_key_name="~", parent=self))
        first_line.addWidget(Key(main_key_name="\"", second_key_name="3", third_key_name="#", parent=self))
        first_line.addWidget(Key(main_key_name="'", second_key_name="4", third_key_name="{", parent=self))
        first_line.addWidget(Key(main_key_name="(", second_key_name="5", third_key_name="[", parent=self))
        first_line.addWidget(Key(main_key_name="-", second_key_name="6", third_key_name="|", parent=self))
        first_line.addWidget(Key(main_key_name="è", second_key_name="7", third_key_name="`", parent=self))
        first_line.addWidget(Key(main_key_name="_", second_key_name="8", third_key_name="\\", parent=self))
        first_line.addWidget(Key(main_key_name="ç", second_key_name="9", third_key_name="^", parent=self))
        first_line.addWidget(Key(main_key_name="à", second_key_name="0", third_key_name="@", parent=self))
        first_line.addWidget(Key(main_key_name=")", second_key_name="°", third_key_name="]", parent=self))
        first_line.addWidget(Key(main_key_name="=", second_key_name="+", third_key_name="}", parent=self))
        first_line.addWidget(Key(main_key_name="←", width=300, parent=self))

        return first_line

    def create_second_line(self):
        second_line = QHBoxLayout()

        second_line.addWidget(Key(main_key_name="↹", width=200, parent=self))
        second_line.addWidget(Key(main_key_name="a", parent=self))
        second_line.addWidget(Key(main_key_name="z", parent=self))
        second_line.addWidget(Key(main_key_name="e", parent=self))
        second_line.addWidget(Key(main_key_name="r", parent=self))
        second_line.addWidget(Key(main_key_name="t", parent=self))
        second_line.addWidget(Key(main_key_name="y", parent=self))
        second_line.addWidget(Key(main_key_name="u", parent=self))
        second_line.addWidget(Key(main_key_name="i", parent=self))
        second_line.addWidget(Key(main_key_name="o", parent=self))
        second_line.addWidget(Key(main_key_name="p", parent=self))
        second_line.addWidget(Key(main_key_name="^", second_key_name="¨", parent=self))
        second_line.addWidget(Key(main_key_name="$", second_key_name="£", third_key_name="¤", parent=self))
        second_line.addWidget(Key(main_key_name=" ", width=200, parent=self))

        return second_line

    def create_third_line(self):
        third_line = QHBoxLayout()

        third_line.addWidget(Key(main_key_name="🔒", width=220, hasLed=True, parent=self))
        third_line.addWidget(Key(main_key_name="q", parent=self))
        third_line.addWidget(Key(main_key_name="s", parent=self))
        third_line.addWidget(Key(main_key_name="d", parent=self))
        third_line.addWidget(Key(main_key_name="f", parent=self))
        third_line.addWidget(Key(main_key_name="g", parent=self))
        third_line.addWidget(Key(main_key_name="h", parent=self))
        third_line.addWidget(Key(main_key_name="j", parent=self))
        third_line.addWidget(Key(main_key_name="k", parent=self))
        third_line.addWidget(Key(main_key_name="l", parent=self))
        third_line.addWidget(Key(main_key_name="m", parent=self))
        third_line.addWidget(Key(main_key_name="ù", second_key_name="%", parent=self))
        third_line.addWidget(Key(main_key_name="*", second_key_name="µ", parent=self))
        third_line.addWidget(Key(main_key_name="Enter", width=180, parent=self))

        return third_line

    def create_fourth_line(self):
        fourth_line = QHBoxLayout()

        fourth_line.addWidget(Key(main_key_name="⇧", parent=self))
        fourth_line.addWidget(Key(main_key_name="<", second_key_name=">", parent=self))
        fourth_line.addWidget(Key(main_key_name="w", parent=self))
        fourth_line.addWidget(Key(main_key_name="x", parent=self))
        fourth_line.addWidget(Key(main_key_name="c", parent=self))
        fourth_line.addWidget(Key(main_key_name="v", parent=self))
        fourth_line.addWidget(Key(main_key_name="b", parent=self))
        fourth_line.addWidget(Key(main_key_name="n", parent=self))
        fourth_line.addWidget(Key(main_key_name=",", second_key_name="?", parent=self))
        fourth_line.addWidget(Key(main_key_name=";", second_key_name=".", parent=self))
        fourth_line.addWidget(Key(main_key_name=":", second_key_name="/", parent=self))
        fourth_line.addWidget(Key(main_key_name="!", second_key_name="§", parent=self))
        fourth_line.addWidget(Key(main_key_name="⇧", width=400, parent=self))

        return fourth_line

    def create_fifth_line(self):
        fifth_line = QHBoxLayout()

        fifth_line.addWidget(Key(main_key_name="ctrl", parent=self))
        fifth_line.addWidget(Key(main_key_name="fn", parent=self))
        fifth_line.addWidget(Key(main_key_name="⊞", parent=self))
        fifth_line.addWidget(Key(main_key_name="alt", parent=self))
        fifth_line.addWidget(Key(main_key_name="Space", width=600, parent=self))
        fifth_line.addWidget(Key(main_key_name="alt gr", hasLed=True, parent=self))
        fifth_line.addWidget(Key(main_key_name="fn", parent=self))
        fifth_line.addWidget(Key(main_key_name="ctrl", parent=self))

        fifth_line.addWidget(Key(main_key_name="🠔", parent=self))

        bottom_top_arrow_layout = QVBoxLayout()
        bottom_top_arrow_layout.addWidget(Key(main_key_name="🠕", height=48, parent=self))
        bottom_top_arrow_layout.addWidget(Key(main_key_name="🠗", height=48, parent=self))

        fifth_line.addLayout(bottom_top_arrow_layout)
        fifth_line.addWidget(Key(main_key_name="➝", parent=self))

        return fifth_line

    def update_color_respiration(self):
        if self.red == 255 and self.green < 255 and self.blue == 0:
            self.green += 1
        elif self.red > 0 and self.green == 255 and self.blue == 0:
            self.red -= 1
        elif self.red == 0 and self.green == 255 and self.blue < 255:
            self.blue += 1
        elif self.red == 0 and self.green > 0 and self.blue == 255:
            self.green -= 1
        elif self.red < 255 and self.green == 0 and self.blue == 255:
            self.red += 1
        elif self.red == 255 and self.green == 0 and self.blue > 0:
            self.blue -= 1

        self.update_qss()

    def update_qss(self):

        reading_file = open("./style.qss", "r")

        new_file_content = ""
        current_element = ""
        for line in reading_file:
            stripped_line = line.strip()
            new_line = stripped_line

            if ";" not in line and "{" in line:
                current_element = line

            if "color" == line.split(":")[0] and "Char" in current_element:
                new_line = "color: rgb(" + str(self.red) + ", " + str(self.green) + ", " + str(self.blue) + ");"
            new_file_content += new_line + "\n"
        reading_file.close()

        writing_file = open("./style.qss", "w")
        writing_file.write(new_file_content)
        writing_file.close()

        self.setStyleSheet(open('./style.qss').read())

    def handle_click(self):
        print("here")
