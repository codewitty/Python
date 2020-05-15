# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# In-Class Assignment F


def hello():
	'This function prints the message "Hello World"'
	print (f'Hello World')

def printListElement(a_list, a_num):
	try:
		print(f'The element at index {a_num} is {a_list.index(a_num)}')
	except:
		print(f'Error: bad index number.')

def main():
	hello()
	#help(hello)
	myInt = 3
	myList = [0, 1, 2]

	printListElement(myList, 3)

	print (f'Original ID of myInt in main is {id(myInt)}') 
	print (f'Original ID of myList in main is {id(myList)}')
	print (f'Original ID of myList\'s last element in main is {id(myList[len(myList)-1])}')

	def byVal(arg1):
		print (f'Original ID of parameter in byVal {id(arg1)}')
		arg1 += 7
		print (f'ID of parameter in byVal after change {id(arg1)}')

	def byRef(arg2):
		print (f'Original ID of parameter in byRef {id(arg2)}')
		print (f'Original ID of parameter\'s last element in byRef is {id(arg2[len(arg2)-1])}')
		arg2[len(arg2)-1] += 7
		print (f'ID of parameter in byRef after change {id(arg2)}')
		print (f'ID of parameter\'s last element in byRef after change is {id(arg2[len(arg2)-1])}')

	byVal(myInt)
	byRef(myList)

	print (f'ID of myInt in main after call to byVal is {id(myInt)}')
	print (f'ID of myList in main after call to byRef is {id(myList)}')
	print (f'ID of myList\'s last element after call to byRef is {id(myList[len(myList)-1])}')

	print (f'myInt is now: {myInt}')
	print (f'myList is now: {myList}')


if __name__ == '__main__':
    main()

'''
Execution results:
Hello World

Help on function hello in module __main__:

hello()
    This function prints the message "Hello World"

Error: bad index number.
Original ID of myInt in main is 4323487568
Original ID of myList in main is 4329166320
Original ID of myList's last element in main is 4323487536
Original ID of parameter in byVal 4323487568
ID of parameter in byVal after change 4323487792
Original ID of parameter in byRef 4329166320
Original ID of parameter's last element in byRef is 4323487536
ID of parameter in byRef after change 4329166320
ID of parameter's last element in byRef after change is 4323487760
ID of myInt in main after call to byVal is 4323487568
ID of myList in main after call to byRef is 4329166320
ID of myList's last element after call to byRef is 4323487760
myInt is now: 3
myList is now: [0, 1, 9]
'''
