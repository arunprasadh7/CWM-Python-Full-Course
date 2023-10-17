# 2 Creating classes
# naming classes - Pascal naming convention - first letter of ever word is capital and no underscore allowed

class Point:
	def draw(self):
		print('Started drawing..')

p1 = Point()
p1.draw()
print(type(p1))
print(isinstance(p1,Point))