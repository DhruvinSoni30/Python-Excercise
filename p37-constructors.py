class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Move")
    def draw(self):
        print("Draw")

point = Point(10,20)
print(point.x)

point.x = 11
print(point.x)