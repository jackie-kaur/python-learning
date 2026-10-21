import rectangle

class Square(rectangle.Rectangle):
    def __init__(self, oneSide):
        super().__init__(oneSide, oneSide)

    def getArea(self):
        return self.side1 * self.side2

    def getPerimeter(self):
        return self.side1 * 4

    def __str__(self):
        return f"I am a square. My side lengths is {self.side1}."