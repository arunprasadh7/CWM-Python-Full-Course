# 4 Class vs instance Attributes

class Point:
    default_color = 'red'

    def __init__(self,x,y):
        self.x= x
        self.y = y

    def draw(self):
        print('Drawing...')
        print(f'Point ({self.x},{self.y})')

# creating instances
Point.default_color = 'yellow'

p1 = Point(1,2)
p1.draw()
print(Point.default_color)
print(p1.default_color)

p2 = Point(5,10)
p2.draw()
print(p2.default_color)