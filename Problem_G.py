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
		pres_dict.update({line[0]: line[1]})

if __name__ == '__main__':
    main()
