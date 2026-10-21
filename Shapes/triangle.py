import shape

class Triangle(shape.Shapes):
    base = 0
    height = 0
    width = 0

    def __init__(self, base, height, width):
            self.base = base
            self.height = height
            self.width = width

    def getArea(self):
        return self.base * self.height * 1/2

    def getPerimeter(self):
        return self.base + self.height + self.width

    def __str__(self):
        return f"I am a triangle. One of my sides lengths is {self.base}. My other side length is {self.height}. My last side length is {self.width}."