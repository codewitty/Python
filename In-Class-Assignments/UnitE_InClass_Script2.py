# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# In-Class Assignment Unit E

# Script 2

# Using range with a for loop 

for x in range(10, -1, -2):
	print(x)

# Looping through dictionary items

movies = {'The Wizard of Oz': '1939' , 'The Godfather': '1972' , 
			'Lawrence of Arabia': '1962' , 'Raging Bull': '1980'}

for movie in sorted(movies):
	print (f'{movie} was made in {movies.get(movie)}')



'''
Execution Results:

10
8
6
4
2
0
Lawrence of Arabia was made in 1962
Raging Bull was made in 1980
The Godfather was made in 1972
The Wizard of Oz was made in 1939

'''
