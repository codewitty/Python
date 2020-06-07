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
			print (f'Sorry {self.name} you are at your limit of {self.checkOutLimit} books')

	def returnBook(self, book):
		bookName = book[0]
		self.booksCheckedOut.remove(bookName)
		print (f'{self.name} has returned {bookName}')
		self.checkOutLimit += 1

	def printCheckedOutBooks(self):
			print (f'{self.name} has the following books checked out:')
			print (f' {self.booksCheckedOut}')

class AdultPatron(LibraryPatron):
	def __init__(self, name):
		LibraryPatron.__init__(self, name)
		self.checkOutLimit = 4

	def checkOutBook(self, book):
		if (self.checkOutLimit >= 1):
			LibraryPatron.checkOutBook(self, self.checkOutLimit, book[0])
			self.checkOutLimit -= 1
		else:
			print (f'Sorry {self.name} you are at your limit of 4 books')

class JuvenilePatron(LibraryPatron):
	def __init__(self, name):
		LibraryPatron.__init__(self, name)
		self.checkOutLimit = 2

	def checkOutBook(self, book):
		if (book[1] == "Adult"):
			print (f'Sorry {self.name} this is book is only for adult patrons.') 

		elif (self.checkOutLimit >= 1 and book[1] == "Juvenile"):
			LibraryPatron.checkOutBook(self, self.checkOutLimit, book[0])
			self.checkOutLimit -= 1

		else:
			print (f'Sorry {self.name} you are at your limit of 2 books')

def main():

	book1 = ["Alice in Wonderland", "Juvenile"]
	book2 = ["The Cat in the Hat", "Juvenile"]
	book3 = ["Harry Potter and the Sorcerer's Stone", "Juvenile"]
	book4 = ["The Hobbit", "Juvenile"]
	book5 = ["The Da Vinci Code", "Adult"]
	book6 = ["The Girl with the Dragon Tattoo", "Adult"]


	patron1 = JuvenilePatron("Jimmy")
	patron2 = AdultPatron("Sophia")

	patron1.checkOutBook(book6)
	patron1.checkOutBook(book1)
	patron1.checkOutBook(book2)
	patron1.printCheckedOutBooks()
	patron1.checkOutBook(book3)
	patron1.returnBook(book1)
	patron1.checkOutBook(book3)
	patron1.printCheckedOutBooks()
	patron2.checkOutBook(book5)
	patron2.checkOutBook(book4)
	patron2.printCheckedOutBooks()


if __name__ == '__main__':
    main()

'''
Execution Results:

Circle area is: 50.27
Cylinder volume is: 62.83

'''
