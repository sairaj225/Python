# Adding Two points

class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        print(f"Point object is created: P({self.x, self.y})")

    # Overloading + operator
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    # Overloading - operator
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __str__(self):
        return f"P({self.x}, {self.y})"

point1 = Point(2, 5)
point2 = Point(8, 4)

point3 = point1 + point2
point4 = point1 - point2
print(point3)
print(point4)
