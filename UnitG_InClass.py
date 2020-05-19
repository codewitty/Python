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

Beautiful is better than ugly.
Explicit is better than implicit.
Readability counts.
If the implementation is hard to explain, it's a bad idea.
Athens Georgia 115452
Athens Ohio 23832
Berlin Connecticut 19866
Berlin Wisconsin 5524
Dublin California 46036
Dublin Ohio 41751
Glasgow Connecticut 11951
Glasgow Kentucky 14028
London Kentucky 7993
London Ohio 9904
Milan Illinois 5099
Milan Michigan 5836
Milan Tennessee 7851
Paris Kentucky 8553
Paris Tennessee 10156
Paris Texas 25171
Warsaw Indiana 13559
Warsaw New York 5064
Please enter a city:Dublin
Please enter a state:California
Dublin California has a population of 46036
'''
