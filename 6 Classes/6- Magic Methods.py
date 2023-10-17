# 6- Magic Methods- double underscore
class Point:
    default_color = 'red'

    def __init__(self,x,y):
        self.x= x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def draw(self):
        print('Drawing...')
        print(f'Point ({self.x},{self.y})')


p1 = Point(1,2)
print(p1)
print(str(p1))


