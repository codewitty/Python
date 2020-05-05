import copy
import math

#x = int(input(f'Enter a number\n'))


#print (f'{round(math.sqrt(x),2)}')

'''
var1 = "python"

print (f'{len(var1)}')

print()

print (f'{var1[2:4]}')

y = var1[3]

print (y)

m = 45

print (f'{m:>8.2f}')

list1 = [1, 2, 3, 4]

list1.sort()

print (f'{list1}')

print (f'{max(list1)}')

x = list1.pop(list1.index(3))

print (f'{x}')

print (f'{list1}')

list1 = [1, 2, 3]

list2 = list1

print (f'{list1 == list2}')

print (f'{list1 is (list2)}')

list3 = copy.deepcopy(list1)


print (f' 3: {list1 == list3}')
print (f'{list1 is (list3)}')
'''
list1 = [1, 2, 3]

list2 = list1

list3 = [list1, list2]

print (f'{list3[1][0]}')
