import shape

class Rectangle(shape.Shapes):
    side1 = 0
    side2 = 0

    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def getArea(self):
        return self.side1 * self.side2

    def getPerimeter(self):
        return self.side1 + self.side1 + self.side2 + self.side2

    def __str__(self):
        return f"I am a rectangle. One of my sides lengths is {self.side1}. My other side length is {self.side2}."