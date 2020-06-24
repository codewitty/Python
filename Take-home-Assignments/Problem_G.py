# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Take Home Assignment G

def main():

# Part One
	f = open('States.txt', 'rt')
	maxPop = 0
	maxState = ''

	for x in f:
		line = x.split()
		pop = int(line[2])
		if line[1] == 'Midwest' and pop > maxPop:
			maxPop = pop
			maxState = line[0]
	print(f'Highest population state in the Midwest is: {maxState} {maxPop}.')

	f.close()

# Part Two – A Dictionary of LisortedList

	f = open('USPresidents.txt', 'rt')
	pres_dict = {}

	for x in f:
		line = x.split()
		if line[0] in pres_dict:
		  pres_dict[line[0]].append(line[1])
		else:
		  pres_dict[line[0]] = [line[1]]

	f.close()
	maxcount = max(len(v) for v in pres_dict.values())

	for k, v in pres_dict.items():
		if len(v) == maxcount:
			print (f'The state with the most presidents is {k} with {maxcount} presidents:')	
			print(*pres_dict.get(k), sep = "\n")
		
# Part Three – – Dictionary Keys and Sets

	f = open('USPresidents.txt', 'rt')
	presidentCount_dict = {}

	for x in f:
		line = x.split()
		if line[0] in presidentCount_dict:
		  presidentCount_dict[line[0]].append(line[1])
		else:
		  presidentCount_dict[line[0]] = [line[1]]
	
	for state in presidentCount_dict:
		if state in presidentCount_dict:
			presidentCount_dict[line[0]] += 1
		else:
			presidentCount_dict[line[0]] = 1
		# presidentCount_dict[k] = len(v)

	highPopStates = {'CA', 'TX', 'FL', 'NY', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI'}
	highPopStates_wPresidents = set(pres_dict) & highPopStates
	print (f'{len(highPopStates_wPresidents)} of the 10 high population states have had presidents born in them:')

	sortedList = sorted(highPopStates_wPresidents)

	for state in sortedList:
		print(f'{state} {presidentCount_dict[state]}')

	f.close()

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
