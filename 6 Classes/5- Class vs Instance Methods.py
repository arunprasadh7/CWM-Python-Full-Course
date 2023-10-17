# 5- Class vs Instance Methods

class Point:
    default_color = 'red'

    def __init__(self,x,y):
        self.x= x
        self.y = y

    def draw(self):
        print('Drawing...')
        print(f'Point ({self.x},{self.y})')

    @classmethod
    def zero(cls):
        return cls(0,0)

p1 = Point.zero()
p1.draw()
