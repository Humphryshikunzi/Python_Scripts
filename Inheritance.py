class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        area = 3.142*(float)self.radius*(float)self.radius
        print('The area is ',area)
        return 0

circle_one = Circle.area()