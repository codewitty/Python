# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Take-Home Assignment I

class Square:
	def __init__(self, side):
		self.side = side

	def getArea(self):
		return self.side * self.side

class Cube(Square):
	def __init__(self, side):
		Square.__init__(self, side)

	def getVolume(self):
		return self.side * self.side * self.side

def calcTotal(price, taxRate = 0.08):
	return price + (price * taxRate)

def main():

	s = Square(3)
	print (f'{s.getArea()}')
	c = Cube(4)
	print (f'{c.getVolume()}')
	print (f'{calcTotal(10)}')
	myLists = []

	for row in range(1,6,2):

		newRow = []

		for col in range(1,6,2):

			newRow.append(row*col**2)

		myLists.append(newRow)

	print(myLists[0][1])

if __name__ == '__main__':
    main()

'''
Execution Results:

Sorry Jimmy this is book is only for adult patrons.
Jimmy has checked out Alice in Wonderland
Jimmy has checked out The Cat in the Hat
Jimmy has the following books checked out:
Alice in Wonderland
The Cat in the Hat
Sorry Jimmy you are at your limit of 2 books
Jimmy has returned Alice in Wonderland
Jimmy has checked out Harry Potter and the Sorcerer's Stone
Jimmy has the following books checked out:
The Cat in the Hat
Harry Potter and the Sorcerer's Stone
Sophia has checked out The Da Vinci Code
Sophia has checked out The Hobbit
Sophia has the following books checked out:
The Da Vinci Code
The Hobbit

'''
