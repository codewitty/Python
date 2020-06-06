# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# In-Class Assignment I

import math

class LibraryPatron:
	def __init__(self, name):
		self.name = name
		self.booksCheckedOut = []

	def checkOutBook(self, checkOutLimit, bookTitle):
		if (checkOutLimit >= 1):
			self.booksCheckedOut.append(bookTitle)
			print (f'{self.name} has checked out {bookTitle}')
		else:
			print (f'Sorry {self.name} you are at your limit of {checkOutLimit} books')

	def returnBook(self, book):
		bookName = book[0]
		self.booksCheckedOut.pop[bookName]
		
		print (f'{self.name} has returned {bookName}')

class AdultPatron(LibraryPatron):
	def __init__(self, name):
		Circle.__init__(self, name)
		self.checkOutLimit = 4

	def checkOutBook(self, book):
		if (checkOutLimit >= 1):
			self.booksCheckedOut.append(bookTitle)
			print (f'{self.name} has checked out {bookTitle}')
		else:
			print (f'Sorry {self.name} you are at your limit of {checkOutLimit} books')
	def getVolume(self):
		return Circle.getArea(self) * self.height

def main():

	circle = Circle(4)
	print (f'Circle area is: {circle.getArea():.2f}')
	print(circle.radius)
	print(circle.getArea())
	cylinder = Cylinder(2, 5)
	print (f'Cylinder volume is: {cylinder.getVolume():.2f}')

if __name__ == '__main__':
    main()

'''
Execution Results:

Circle area is: 50.27
Cylinder volume is: 62.83

'''
