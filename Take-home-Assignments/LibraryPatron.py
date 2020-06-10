# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# In-Class Assignment J

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

	def returnBook(self, Book):
		bookName = Book.self.title 
		self.booksCheckedOut.remove(bookName)
		print (f'{self.name} has returned {bookName}')
		self.checkOutLimit += 1

	def printCheckedOutBooks(self):
			print (f'{self.name} has the following books checked out:')
			for x in range(len(self.booksCheckedOut)):
				print (f'{self.booksCheckedOut[x]}')

class AdultPatron(LibraryPatron):
	def __init__(self, name):
		LibraryPatron.__init__(self, name)
		self.checkOutLimit = 4

	def checkOutBook(self, Book):
		if (self.checkOutLimit >= 1):
			LibraryPatron.checkOutBook(self, self.checkOutLimit, LibraryBook.Book.self.title)
			self.checkOutLimit -= 1
		else:
			print (f'Sorry {self.name} you are at your limit of 4 books')

class JuvenilePatron(LibraryPatron):
	def __init__(self, name):
		LibraryPatron.__init__(self, name)
		self.checkOutLimit = 2

	def checkOutBook(self, book):
		if (LibraryBook.Book.self.bookType == "Adult"):
			print (f'Sorry {self.name} this is book is only for adult patrons.') 

		elif (self.checkOutLimit >= 1 and LibraryBook.Book.self.bookType == "Juvenile"):
			LibraryPatron.checkOutBook(self, self.checkOutLimit, LibraryBook.Book.self.title)
			self.checkOutLimit -= 1

		else:
			print (f'Sorry {self.name} you are at your limit of 2 books')

