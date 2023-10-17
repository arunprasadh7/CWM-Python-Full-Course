# 4- Class vs Instance Attributes

class Point:
	default_color = 'red'

    def __init__(self, x, y):	#constructor
        self.x = x	#instance attribute
        self.y = y 

    def draw(self):
    	print('Drawing..')
    	print(f'Point ({self.x},{self.y})')

# first instance
p1 = Point(1,2)
print(p1.x)
print(p1.y)
p1.draw()

# second instance
p2 = Point(5,5)
p2.draw()