class Complex:
    def __init__(self, re: float, im: float) -> None:
        """
        :param re: real part with exception handling
        :param im: imaginary part with exception handling
        """
        if re == "":
            self.re = 0
        else:
            try:
                self.re = int(re)
            except ValueError:
                try:
                    self.re = round(float(re),3)
                except ValueError:
                    raise ValueError
        if im == "":
            self.im = 0
        else:
            try:
                self.im = int(im)
            except ValueError:
                try:
                    self.im = round(float(im),3)
                except ValueError:
                    raise ValueError



    def __neg__(self):
        return Complex(self.re, -1 * self.im)

    def __add__(self, other):
        new_re = self.re + other.re
        new_im = self.im + other.im
        return Complex(new_re, new_im)

    def __sub__(self, other):
        new_re = self.re - other.re
        new_im = self.im - other.im
        return Complex(new_re, new_im)

    def __mul__(self, other):
        new_re = (self.re * other.re) - (self.im * other.im)
        new_im = (self.re * other.im) + (self.im * other.re)
        return Complex(new_re, new_im)

    def __truediv__(self, other):
        t = self * (-other)
        c = (other.re * other.re) + (other.im * other.im)
        new_re = t.re / c
        new_im = t.im / c
        return Complex(new_re, new_im)

    def __round__(self, n=None):
        return self

    def __str__(self):
        return f'{self.re} + {self.im}i'