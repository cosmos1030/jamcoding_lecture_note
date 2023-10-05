class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height

rect1 = Rect(10,20)
print(rect1.get_area())

class Square(Rect):
    def __init__(self, side):
        self.width = side
        self.height = side

square1 = Square(10)
print(square1.get_area())