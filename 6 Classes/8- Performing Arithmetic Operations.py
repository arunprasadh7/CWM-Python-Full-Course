#8- Performing Arithmetic Operations

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y =y

    def __add__(self, other):
        return Point(self.x + other.x,self.y + other.y)

p1 = Point(1,1)
p2 = Point(2,2)
combined = p1+p2
print(combined.x)
print(combined.y)