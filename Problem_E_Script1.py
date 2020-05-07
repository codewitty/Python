# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Unit D take-home assignment

# Part One - Sets
from collections import namedtuple

class1 = {'Li', 'Audry', 'Jia', 'Migel', 'Tanya'}
class2 = {'Sasha', 'Migel', 'Tanya', 'Hiroto', 'Audry'}
class3 = {'Migel', 'Zhang', 'Hiroto', 'Anita', 'Jia'}

print (f'Students in all three classes: {sorted(class1 & class2 & class3)}')
print (f'All students: {sorted(class1 | class2 | class3)}')
print (f'Students in class1 but not class2 or class3: {sorted((class1 - class2) & (class1 - class3))}')

# Part Two - Swap

list1 = [1, 2, 3]
list1[1],list1[2] = list1[2], list1[1]
print (f'List after swap: {list1}')

# Part Three – Tuple Basics

movie = ('Casablanca', '1942', 'romantic drama')
title, year, genre = movie

print (f'My favorite movie is: {title}')

# Part Four - Named Tuple
Movie = namedtuple('Movie', 'title year genre')
favMovie = Movie(title = "Casablanca", year = 1942, genre = "romantic drama")
print (f'My favorite movie is: {favMovie.title}')

# Part Five - Named Tuple Containing a List
Moviestars = namedtuple('Moviestars', 'title year genre stars')
favoritemovie = Moviestars(title = "Casablanca", year = 1942, genre = "romantic drama", stars = ['Humphrey Bogart', 'Ingrid Bergman'])
favoritemovie.stars.append('Claude Rains')
print (f'My favorite star is: {favoritemovie.stars[1]}')
print (f'{favoritemovie}')

'''
Execution Results:

Students in all three classes: ['Migel']
All students: ['Anita', 'Audry', 'Hiroto', 'Jia', 'Li', 'Migel', 'Sasha', 'Tanya', 'Zhang']
Students in class1 but not class2 or class3: ['Li']
List after swap: [1, 3, 2]
My favorite movie is: Casablanca
My favorite movie is: Casablanca
My favorite star is: Ingrid Bergman
Moviestars(title='Casablanca', year=1942, genre='romantic drama', stars=['Humphrey Bogart', 'Ingrid Bergman', 'Claude Rains'])
'''
