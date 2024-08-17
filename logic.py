from PyQt6.QtWidgets import *
from gui import *
from Complex import *
from Vector import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        """
        initialize the display_text, decimal_counter, memory, and operation variables
        connect functions to all buttons on the gui
        hide the z-vector buttons
        """
        super().__init__()
        self.setupUi(self)

        self.display_text = ' '
        self.dec_counter = 0
        self.mem = 0
        self.operation = 'n'

        self.button_c.clicked.connect(lambda: self.clear())
        self.button_ce.clicked.connect(lambda: self.full_clear())
        self.button_plus.clicked.connect(lambda: self.submit_button_opp('a'))
        self.button_sub.clicked.connect(lambda: self.submit_button_opp('s'))
        self.button_times.clicked.connect(lambda: self.submit_button_opp('t'))
        self.button_div.clicked.connect(lambda: self.submit_button_opp('d'))
        self.button_per.clicked.connect(lambda: self.submit_button_opp('m'))
        self.button_eql.clicked.connect(lambda: self.submit_button_eql())
        self.button_inv.clicked.connect(lambda: self.submit_button_inverse())
        self.button_square.clicked.connect(lambda: self.submit_button_square())
        self.button_root.clicked.connect(lambda: self.submit_button_root())

        self.button_0.clicked.connect(lambda: self.submit_button_number('0'))
        self.button_1.clicked.connect(lambda: self.submit_button_number('1'))
        self.button_2.clicked.connect(lambda: self.submit_button_number('2'))
        self.button_3.clicked.connect(lambda: self.submit_button_number('3'))
        self.button_4.clicked.connect(lambda: self.submit_button_number('4'))
        self.button_5.clicked.connect(lambda: self.submit_button_number('5'))
        self.button_6.clicked.connect(lambda: self.submit_button_number('6'))
        self.button_7.clicked.connect(lambda: self.submit_button_number('7'))
        self.button_8.clicked.connect(lambda: self.submit_button_number('8'))
        self.button_9.clicked.connect(lambda: self.submit_button_number('9'))

        self.button_dec.clicked.connect(lambda: self.submit_button_dec())
        self.button_pm.clicked.connect(lambda: self.submit_button_pm())
        self.button_back.clicked.connect(lambda: self.submit_button_back())

        self.radio_button_3D.clicked.connect(lambda: self.show_z())
        self.radio_button_2D.clicked.connect(lambda: self.hide_z())

        self.button_vector_plus.clicked.connect(lambda: self.submit_button_vector('a'))
        self.button_vector_sub.clicked.connect(lambda: self.submit_button_vector('s'))
        self.button_vector_times.clicked.connect(lambda: self.submit_button_vector('t'))
        self.button_vector_div.clicked.connect(lambda: self.submit_button_vector('d'))

        self.button_complex_plus.clicked.connect(lambda: self.submit_button_complex('a'))
        self.button_complex_sub.clicked.connect(lambda: self.submit_button_complex('s'))
        self.button_complex_times.clicked.connect(lambda: self.submit_button_complex('t'))
        self.button_complex_div.clicked.connect(lambda: self.submit_button_complex('d'))

        self.hide_z()

    def check_error(self) -> None:
        """
        check if Error is being displayed
        if so full clear
        """
        if self.display_text == 'Error':
            self.full_clear()

    def full_clear(self) -> None:
        """
        clear all displays and entries
        set memory to zero and operation to none
        """
        self.clear()
        self.operation = 'n'
        self.mem = 0

    def clear(self) -> None:
        """
        clear the display and all text entries
        """
        self.display_text = ' '
        self.dec_counter = 0
        self.display.setText(self.display_text)
        self.entry_vector_u_x.setText("")
        self.entry_vector_v_x.setText("")
        self.entry_vector_u_y.setText("")
        self.entry_vector_v_y.setText("")
        self.entry_vector_u_z.setText("")
        self.entry_vector_v_z.setText("")
        self.entry_complex_w_im.setText("")
        self.entry_complex_z_im.setText("")
        self.entry_complex_w_re.setText("")
        self.entry_complex_z_re.setText("")

    def check_length(self) -> bool:
        """
        Method to check if display text is less than or equal 10 numbers
        Need extra space for pos/neg sign
        :return: True or False
        """
        if len(self.display_text) <= 11:
            return True
        else:
            return False

    def hide_z(self) -> None:
        """
        hide all z-vector entries
        set text to nothing in z-text entries
        """
        self.label_vector_u_z.hide()
        self.label_vector_v_z.hide()
        self.entry_vector_u_z.hide()
        self.entry_vector_v_z.hide()
        self.entry_vector_u_z.setText("")
        self.entry_vector_v_z.setText("")

    def show_z(self) -> None:
        """
        show all z-vector entries
        """
        self.label_vector_u_z.show()
        self.label_vector_v_z.show()
        self.entry_vector_u_z.show()
        self.entry_vector_v_z.show()

    def submit_button_number(self, text: str = "") -> None:
        """
        append the display_text with the number being pressed
        check if error or scientific are being displayed and clear accordingly
        :param text: number on the button being pressed
        """
        self.check_error()
        if self.check_scientific():
            self.clear()
        if self.check_length():
            self.display_text = self.display_text + text
            self.display.setText(self.display_text)
        else:
            pass

    def submit_button_dec(self) -> None:
        """
        append the display_text with a decimal
        only one decimal can be displayed at a time
        check for error handling
        """
        self.check_error()
        if self.dec_counter == 0:
            self.display_text = self.display_text + '.'
            self.dec_counter += 1
        else:
            pass

    def submit_button_pm(self) -> None:
        """
        at beginning of display_text change from " " to "-"
        or from "-" to " "
        check for error handling
        """
        self.check_error()
        if self.display_text[0] == " ":
            self.display_text = '-' + self.display_text[1:]
        else:
            self.display_text = " " + self.display_text[1:]
        self.display.setText(self.display_text)

    def submit_button_back(self) -> None:
        """
        delete the last digit in the display_text
        keep the " " or "-" at the beginning of the text
        check for error and scientific and handle accordingly
        """
        self.check_error()
        if self.check_scientific():
            self.clear()

        else:
            if len(self.display_text) > 1:
                if self.display_text[-2] == '.':
                    self.dec_counter -= 1
                    self.display_text = self.display_text[:-2]
                    self.display.setText(self.display_text)
                else:
                    self.display_text = self.display_text[:-1]
                    self.display.setText(self.display_text)

            else:
                pass

    def submit_button_opp(self, opp: str = 'n') -> None:
        """
        when clicking an operation store current value in memory either as an int or a float
        clear display text and save the operation selected
        error handling
        :param opp: specifies which operation has been chosen
        """
        self.check_error()
        if self.operation != 'n':
            self.submit_button_eql()
        self.check_error()
        self.operation = opp
        if self.display_text == " " or self.display_text == '-':
            self.mem = 0
        else:
            try:
                self.mem = int(self.display.text())
            except ValueError:
                self.mem = float(self.display_text)
        self.clear()

    def submit_button_eql(self, other: float = 0, set: str = 'R') -> None:
        """
        store current display as other and do the corresponding operation and display accordingly
        :param other: this is the current value displayed
        :param set: this is the mathematical set the operation is being done on, R = reals, V = vectors, C = complex
        """
        self.check_error()
        if set != 'R':
            other = other
        elif self.display_text == " " or self.display_text == '-':
            other = 0
        else:
            try:
                other = int(self.display.text())
            except ValueError:
                other = float(self.display_text)
        if self.operation == 'n':
            pass
        elif self.operation == 'a':
            self.display_text = str(self.add(self.mem, other))
        elif self.operation == 's':
            self.display_text = str(self.subtract(self.mem, other))
        elif self.operation == 't':
            self.display_text = str(self.multiply(self.mem, other))
        elif self.operation == 'd':
            self.display_text = str(self.divide(self.mem, other))
        elif self.operation == 'm':
            self.display_text = str(self.mod(self.mem, other))

        if set == 'R':
            if not self.check_length():
                self.display_text = float(self.display_text)
                if self.display_text >= 0:
                    self.display_text = " " + "{:.3e}".format(self.display_text)
                else:
                    self.display_text = "{:.3e}".format(self.display_text)

        self.display.setText(self.display_text)
        self.operation = 'n'
        for i in self.display_text:
            if i == '.':
                self.dec_counter += 1
            else:
                self.dec_counter = self.dec_counter

    def add(self, mem: float = 0, other: float = 0) -> float:
        """
        :param mem: first value
        :param other: second value
        :return: sum of two values
        """
        return round(mem + other, 6)

    def subtract(self, mem: float = 0, other: float = 0) -> float:
        """
        :param mem: first value
        :param other: second value
        :return: difference of two values
        """
        return round(mem - other, 6)

    def multiply(self, mem: float = 0, other: float = 0) -> float:
        """
        :param mem: first value
        :param other: second value
        :return: product of two values
        """
        return round(mem * other, 6)

    def divide(self, mem: float = 0, other: float = 1) -> str | float:
        """
        divide by zero error handling
        :param mem: first value
        :param other: second value
        :return: quotient of two values
        """
        try:
            value = round(mem / other, 6)
        except ZeroDivisionError:
            return 'Error'
        return value

    def mod(self, mem: int = 0, other: int = 1) -> str | int:
        """
        mod zero handling and float error
        :param mem: first value
        :param other: second value
        :return: modulus of two values
        """
        if isinstance(mem, float) or isinstance(other, float):
            return 'Error'
        else:
            try:
                value = mem % other
            except ZeroDivisionError:
                return 'Error'
            return value

    def submit_button_inverse(self) -> None:
        """
        compute and display 1/current number
        keep track of decimals when displaying
        """
        self.check_error()
        if self.display_text == " " or self.display_text == '-':
            self.mem = 0
        else:
            try:
                self.mem = int(self.display.text())
            except ValueError:
                self.mem = float(self.display_text)
        self.display_text = str(self.divide(1, self.mem))
        if not self.check_length():
            self.display_text = float(self.display_text)
            if self.display_text >= 0:
                self.display_text = " " + "{:.3e}".format(self.display_text)
            else:
                self.display_text = "{:.3e}".format(self.display_text)
        self.display.setText(self.display_text)
        for i in self.display_text:
            if i == '.':
                self.dec_counter += 1
            else:
                self.dec_counter = self.dec_counter

    def check_scientific(self) -> bool:
        """
        check if display is scientific
        :return: True or False
        """
        for i in self.display_text:
            if i == 'e':
                return True
        return False

    def submit_button_square(self) -> None:
        """
        compute and display square of current number
        keep track of decimals when displaying
        """
        self.check_error()
        if self.display_text == " " or self.display_text == '-':
            self.mem = 0
        else:
            try:
                self.mem = int(self.display.text())
            except ValueError:
                self.mem = float(self.display_text)
        self.display_text = str(self.multiply(self.mem, self.mem))
        if not self.check_length():
            self.display_text = float(self.display_text)
            if self.display_text >= 0:
                self.display_text = " " + "{:.3e}".format(self.display_text)
            else:
                self.display_text = "{:.3e}".format(self.display_text)
        self.display.setText(self.display_text)
        for i in self.display_text:
            if i == '.':
                self.dec_counter += 1
            else:
                self.dec_counter = self.dec_counter

    def submit_button_root(self) -> None:
        """
        compute and display square root of current number
        keep track of decimals when displaying
        complex number handling
        """
        self.check_error()
        if self.display_text == " " or self.display_text == '-':
            self.mem = 0
        else:
            try:
                self.mem = int(self.display.text())
            except ValueError:
                self.mem = float(self.display_text)
        if self.mem < 0:
            self.display_text = str(Complex(0, round((-1 * self.mem) ** (1 / 2), 5)))
        else:
            self.display_text = str(self.mem ** (1 / 2))
            if not self.check_length():
                self.display_text = float(self.display_text)
                if self.display_text >= 0:
                    self.display_text = " " + "{:.3e}".format(self.display_text)
                else:
                    self.display_text = "{:.3e}".format(self.display_text)

        self.display.setText(self.display_text)
        for i in self.display_text:
            if i == '.':
                self.dec_counter += 1
            else:
                self.dec_counter = self.dec_counter

    def submit_button_vector(self, opp: str = 'n') -> None:
        """
        read and store text entries as a vector object
        2-D, 3-D handling done inside the class
        specify and compute and display the operation selected
        :param opp: specifies which operation has been chosen
        """
        self.check_error()
        try:
            u = Vector(self.entry_vector_u_x.text(), self.entry_vector_u_y.text(), self.entry_vector_u_z.text())
        except ValueError:
            self.display_text = "Error"
            self.display.setText(self.display_text)
            return None
        try:
            v = Vector(self.entry_vector_v_x.text(), self.entry_vector_v_y.text(), self.entry_vector_v_z.text())
        except ValueError:
            self.display_text = "Error"
            self.display.setText(self.display_text)
            return None
        self.check_error()
        self.entry_vector_u_x.setText("")
        self.entry_vector_v_x.setText("")
        self.entry_vector_u_y.setText("")
        self.entry_vector_v_y.setText("")
        self.entry_vector_u_z.setText("")
        self.entry_vector_v_z.setText("")

        self.mem = u
        self.operation = opp
        self.submit_button_eql(v, 'V')

    def submit_button_complex(self, opp: str = 'n') -> None:
        """
        read and store text entries as a complex object
        specify and compute and display the operation selected
        :param opp: specifies which operation has been chosen
        """
        self.check_error()
        try:
            w = Complex(self.entry_complex_w_re.text(), self.entry_complex_w_im.text())
        except ValueError:
            self.display_text = "Error"
            self.display.setText(self.display_text)
            return None
        try:
            z = Complex(self.entry_complex_z_re.text(), self.entry_complex_z_im.text())
        except ValueError:
            self.display_text = "Error"
            self.display.setText(self.display_text)
            return None
        self.check_error()
        self.entry_complex_w_im.setText("")
        self.entry_complex_z_im.setText("")
        self.entry_complex_w_re.setText("")
        self.entry_complex_z_re.setText("")

        self.mem = w
        self.operation = opp
        self.submit_button_eql(z, 'C')
