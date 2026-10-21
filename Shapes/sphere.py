import shape

class Sphere(shape.Shapes):
    r = 0

    def __init__(self, r):
        self.r = r

    def getArea(self):
        return 4 * 3.14 * self.r ** 2

    def getPerimeter(self):
        return 2 * 3.14 * self.r

    def __str__(self):
        return f"I am a sphere. My radius is {self.r}"