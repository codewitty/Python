# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Unit D take-home assignment

# Part One - Sets

class1 = {'Li', 'Audry', 'Jia', 'Migel', 'Tanya'}
class2 = {'Sasha', 'Migel', 'Tanya', 'Hiroto', 'Audry'}
class3 = {'Migel', 'Zhang', 'Hiroto', 'Anita', 'Jia'}

print (f'Students in all three classes: {sorted(class1 & class2 & class3)}')
print (f'All students: {sorted(class1 | class2 | class3)}')
print (f'All students: {sorted((class1 - class2) & (class1 - class3))}')

# Part Two - Swap

list1 = [1, 2, 3]
list1[1],list1[2] = list1[2], list1[1]
print (f'List after swap: {list1}')

# Part Three – Tuple Basics




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
