# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# In-Class Assignment D

# Dictionary Basics 

sweets = {
	 'apple': 'sauce',
	 'peach': 'cobbler',
	 'carrot': 'cake',
	 'strawberry': 'sorbet',
	 'banana': 'cream pie',
	 }

sweets['mango'] = 'sticky rice'
sweets['strawberry'] = 'shortcake'

del sweets['carrot']

print (f'apple dessert is: {(sweets["apple"])}')
print (f'banana dessert exists: {"banana" in sweets}')
print (f'pear dessert exists: {"pear" in sweets}')
print (f'{sweets.keys()}')
print (f'{sweets.values()}')
print (f'{sweets.items()}')

# Combining Dictionaries
capitols1 = {
	 'Alabama': 'Montgomery',
	 'Alaska': 'Juneau',
	 'Arizona': 'Phoenix',
	 'Arkansas': 'Little Rock',
	 }

capitols2 = {
	 'California': 'Sac.',
	 'Colorado': 'Denver',
	 'Connecticut': 'Hartford',
	 }

capitols1.update(capitols2)
print (f'Sorted state capitols: {sorted(capitols1.values())}')

# Set Basics

class1 = {'Li', 'Audry', 'Jia', 'Migel', 'Tanya'}
class2 = {'Sasha', 'Migel', 'Tanya', 'Hiroto', 'Audry'}

class1.add('John')

print (f'Students in both classes: {class1 & class2}')
print (f'All students: {class1 | class2}')
print (f'Sasha is in class1: {"Sasha" in class1}')


'''
Execution Results:

apple dessert is: sauce
banana dessert exists: True
pear dessert exists: False
dict_keys(['apple', 'peach', 'strawberry', 'banana', 'mango'])
dict_values(['sauce', 'cobbler', 'shortcake', 'cream pie', 'sticky rice'])
dict_items([('apple', 'sauce'), ('peach', 'cobbler'), ('strawberry', 'shortcake'), ('banana', 'cream pie'), ('mango', 'sticky rice')])
Sorted state capitols: ['Denver', 'Hartford', 'Juneau', 'Little Rock', 'Montgomery', 'Phoenix', 'Sac.']
Students in both classes: {'Tanya', 'Migel', 'Audry'}
All students: {'Tanya', 'John', 'Sasha', 'Hiroto', 'Jia', 'Audry', 'Li', 'Migel'}
Sasha is in class1: False

'''
