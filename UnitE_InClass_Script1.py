# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# In-Class Assignment Unit E

# Script 1

# Determining the genre of a movie

scifi = ['Alien', 'Solaris', 'Inception', 'Moon']
comedy = ['Borat', 'Idiocracy', 'Superbad', 'Bridesmaids']

user_movie = input('Please enter a movie title: ')

#print (f'{user_movie in scifi}')

if user_movie in scifi:
		print(f'{user_movie} is a scifi movie.')
elif user_movie in comedy:
		print(f'{user_movie} is a comedy movie.')
else:
		print(f'Sorry, I don\'t know what kind of movie {user_movie} is.')

'''
Execution Results:
Please enter a movie title: Moon
Moon is a scifi movie.

Please enter a movie title: Superbad
Superbad is a comedy movie.

Please enter a movie title: Dunkirk
Sorry, I don't know what kind of movie Dunkirk is.
'''
