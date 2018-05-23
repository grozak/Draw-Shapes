class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '[{},{}]'.format(self.x, self.y)


class Polygon:
    def __init__(self, points, color):
        self.points = points
        self.color = color


class Rectangle:
    def __init__(self, point, width, height, color):
        self.point = point
        self.width = width
        self.height = height
        self.color = color


class Square:
    def __init__(self, point, size, color):
        self.point = point
        self.size = size
        self.color = color


class Circle:
    def __init__(self, point, radius, color):
        self.point = point
        self.radius = radius
        self.color = color
