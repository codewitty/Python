# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# In-Class Assignment G

import csv

# Part One
fout = open('ZenOfPython.txt', 'wt')

print(f'Beautiful is better than ugly.\nExplicit is better than implicit.', file=fout)

fout.close()

fout = open('ZenOfPython.txt', 'at')

print (f'Readability counts.\nIf the implementation is hard to explain, it\'s a bad idea.', file = fout)
fout.close()

fin = open('ZenOfPython.txt', 'rt' )
lines = fin.readlines()

for line in lines:
     print(line, end='')

# Part Two

with open('Cities.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['City'], row['State'], row['Population'])

city = input('Please enter a city:')
state = input('Please enter a state:')

with open('Cities.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['City'] == city and row['State'] == state: 
			print(f"{city} {state} has a population of {row['Population']}")


'''
Execution Results:

'''
