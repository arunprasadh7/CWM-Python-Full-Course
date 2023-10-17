#7- Comparing Objects

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y =y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

# Checking if 2 numbers are equal
p1 = Point(1,2)
p2 = Point(1,2)
print(p1 == p2)

#checking for greater than
p3 = Point(10,10)
p4 = Point(5,5)
print(p3 > p4)
print(p3 < p4)

