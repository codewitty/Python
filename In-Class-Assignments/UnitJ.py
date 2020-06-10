# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# In-Class Assignment J

import LibraryBook 
import LibraryPatron

def main():

	b1 = LibraryBook.Book("Alice in Wonderland", "Juvenile")
	b2 = LibraryBook.Book("The Cat in the Hat", "Juvenile")
	b3 = LibraryBook.Book("Harry Potter and the Sorcerer's Stone", "Juvenile")
	b4 = LibraryBook.Book("The Hobbit", "Juvenile")
	b5 = LibraryBook.Book("The Da Vinci Code", "Adult")
	b6 = LibraryBook.Book("The Girl with the Dragon Tattoo", "Adult")


	patron1 = LibraryPatron.JuvenilePatron("Jimmy")
	patron2 = LibraryPatron.AdultPatron("Sophia")

	patron1.checkOutBook(b6)
	patron1.checkOutBook(b1)
	patron1.checkOutBook(b2)
	patron1.printCheckedOutBooks()
	patron1.checkOutBook(b3)
	patron1.returnBook(b1)
	patron1.checkOutBook(b3)
	patron1.printCheckedOutBooks()
	patron2.checkOutBook(b5)
	patron2.checkOutBook(b4)
	patron2.printCheckedOutBooks()


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
