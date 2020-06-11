# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# In-Class Assignment J

class LibraryPatron:
	def __init__(self, name):
		self.name = name
		self.booksCheckedOut = []

	def checkOutBook(self, checkOutLimit, Book):
		bookName = Book.title
		if checkOutLimit > len(self.booksCheckedOut):
			self.booksCheckedOut.append(Book)
			print (f'{self.name} has checked out {bookName}')
		else:
			print (f'Sorry {self.name} you are at your limit of {self.checkOutLimit} books')

	def returnBook(self, Book):
		self.booksCheckedOut.remove(Book)
		print (f'{self.name} has returned {Book.title}')

	def printCheckedOutBooks(self):
			print (f'{self.name} has the following books checked out:')
			for x in self.booksCheckedOut:
				print (f'{x.title}')

class AdultPatron(LibraryPatron):
	def __init__(self, name):
		LibraryPatron.__init__(self, name)
		self.checkOutLimit = 4

	def checkOutBook(self, Book):
		LibraryPatron.checkOutBook(self, self.checkOutLimit, Book)

class JuvenilePatron(LibraryPatron):
	def __init__(self, name):
		LibraryPatron.__init__(self, name)
		self.checkOutLimit = 2

	def checkOutBook(self, Book):
		if (Book.bookType == "Adult"):
			print (f'Sorry {self.name}, {Book.title} is an adult book.') 
		else:
			LibraryPatron.checkOutBook(self, self.checkOutLimit, Book)
