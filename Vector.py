class Vector:
    def __init__(self, x=0, y=0, z=""):
        if x == "":
            self.x = 0
        else:
            try:
                self.x = int(x)
            except ValueError:
                try:
                    self.x = round(float(x),3)
                except ValueError:
                    raise ValueError
        if y == "":
            self.y = 0
        else:
            try:
                self.y = int(y)
            except ValueError:
                try:
                    self.y = round(float(y),3)
                except ValueError:
                    raise ValueError
        if z == "":
            self.z = ""
        else:
            try:
                self.z = int(z)
            except ValueError:
                try:
                    self.z = round(float(z),3)
                except ValueError:
                    raise ValueError

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        if self.z != "":
            new_z = self.z + other.z
        else:
            new_z = ""
        return Vector(new_x, new_y, new_z)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        if self.z != "":
            new_z = self.z - other.z
        else:
            new_z = ""
        return Vector(new_x, new_y, new_z)

    def __mul__(self, other):
        scalar = (self.x + other.x) + (self.y + other.y)
        if self.z != "":
            scalar += (self.z + other.z)
        return scalar

    def __truediv__(self, other : float):
        if self.z == "":
            self.z = 0
            other.z = 0
        new_x = (self.y * other.z) - (self.z * other.y)
        new_y = (self.z * other.x) - (self.x * other.z)
        new_z = (self.x * other.y) - (self.y * other.x)
        return Vector(new_x, new_y, new_z)

    def __str__(self):
        if self.z == '':
            return f'({self.x}, {self.y})'

        else:
            return f'({self.x}, {self.y}, {self.z})'
