# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Take Home Assignment G

def main():

# Part Three – – Dictionary Keys and Sets

	states = {}

	file = open('USPresidents.txt', 'rt')

	for line in file:
		x = line.split()
		if x[0] in states:
			states[x[0]] += 1
		else:
			states[x[0]] = 1
	
	for state in states:
		print(f'{state} : {states.get(state)}')

	file.close()

if __name__ == '__main__':
    main()

'''
Execution Results:

Highest population state in the Midwest is: IL 12802000.
The state with the most presidents is VA with 8 presidents:
George_Washington
James_Madison
James_Monroe
John_Tyler
Thomas_Jefferson
William_Henry_Harrison
Woodrow_Wilson
Zachary_Taylor
8 of the 10 high population states have had presidents born in them:
CA 1
GA 1
IL 1
NC 2
NY 5
OH 7
PA 1
TX 2

'''
