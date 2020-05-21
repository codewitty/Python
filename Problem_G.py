# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Take Home Assignment G

import csv

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

# Part Two – A Dictionary of Lists

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
	prez_dict = {}

	for x in f:
		line = x.split()
		if line[0] in prez_dict:
		  prez_dict[line[0]].append(line[1])
		else:
		  prez_dict[line[0]] = [line[1]]
	
	for k,v in pres_dict.items():
		pres_dict[k] = len(v)
	print (pres_dict)

	st_set = {'CA', 'TX', 'FL', 'NY', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI'}
	st2 = set(pres_dict).intersection(st_set)
	print (f' {len(st2)} of the 10 high population states have had presidents born in them:')

	f.close()



















if __name__ == '__main__':
    main()
