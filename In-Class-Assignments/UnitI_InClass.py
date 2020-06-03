# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# In-Class Assignment I

import math

class Circle:
	def __init__(self, radius):
		self.radius = radius

	def getArea(self):
		return math.pi * math.pow(self.radius, 2)

class Cylinder(Circle):
	def __init__(self, radius, height):
		self.height = height
		Circle.__init__(self,radius)

	def getVolume(self):
		return Circle.getArea(self) * self.height

def main():

	circle = Circle(4)
	print (f'Circle area is: {circle.getArea():.2f}')
	cylinder = Cylinder(2, 5)
	print (f'Cylinder volume is: {cylinder.getVolume():.2f}')

if __name__ == '__main__':
    main()

'''
Execution Results:

Circle area is: 50.27
Cylinder volume is: 62.83

'''
