class Shape:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, d_x, d_y):
        self.x += d_x
        self.y += d_y


class Rectangle(Shape):
    all_rectangles = []

    def __init__(self, a, b, x=0, y=0):
        super().__init__(x, y)
        self.a = a
        self.b = b
        self.__class__.all_rectangles.append(self)

    def area(self):
        return self.a * self.b

    @classmethod
    def total_area(cls):
        total = 0
        for square in cls.all_rectangles:
            total += square.area()
        return total

    @staticmethod
    def rectangles_area():
        total = 0
        for rect in Rectangle.all_rectangles:
            total += rect.area()
        return total


class Square(Rectangle):
    def __init__(self, a, x=0, y=0):
        super().__init__(a, a, x, y)
        