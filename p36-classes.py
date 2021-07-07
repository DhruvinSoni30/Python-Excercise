class Point:
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")


point1 = Point()
point2 = Point()
point1.x = 10
point1.y = 20
point2.x = 1
point2.y = 2
print(point1.x)
print(point2.y)
point1.draw()
point1.move()
