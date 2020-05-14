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
	help(hello)
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
Check ==
list1 == list2:  True
list1 == list3:  True
list2 == list3:  True

Check "is"
list1 is list2:  True
list1 is list3:  False
list2 is list3:  False

Print i.d
List1 ID:  4371886960
List2 ID:  4371886960
List3 ID:  4371966144

List1 printed:  [2, 'goodbye', 4.1, 'hello', 8]
List2 printed:  [2, 'goodbye', 4.1, 'hello', 8]
List3 printed:  [4.1, 'hello']
'''
