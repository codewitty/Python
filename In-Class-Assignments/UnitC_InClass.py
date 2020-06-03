# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# In-Class Assignment C

import copy

list1 = [2, 4.1, 'hello']

list2 = list1

list3 = copy.deepcopy(list1)

print("Check ==")
print("list1 == list2: ", (list1 == list2))
print("list1 == list3: ", (list1 == list3))
print("list2 == list3: ", (list2 == list3))

print()

print("Check \"is\"")
print ("list1 is list2: ", (list1 is list2))
print ("list1 is list3: ", (list1 is list3))
print ("list2 is list3: ", (list2 is list3))

print()
print("Print i.d")
print ("List1 ID: ", id(list1))
print ("List2 ID: ", id(list2))
print ("List3 ID: ", id(list3))
print()

list1.append(8)
list2.insert(1, 'goodbye')
list3.pop(0)

print("List1 printed: ", list1)
print("List2 printed: ", list2)
print("List3 printed: ", list3)

'''
Execution results:
Check ==
list1 == list2:  True
list1 == list3:  True
list2 == list3:  True

Check "is"
list1 is list2:  True
list1 is list3:  False
list2 is list3:  False

Print i.d
List1 ID:  4371886960
List2 ID:  4371886960
List3 ID:  4371966144

List1 printed:  [2, 'goodbye', 4.1, 'hello', 8]
List2 printed:  [2, 'goodbye', 4.1, 'hello', 8]
List3 printed:  [4.1, 'hello']
'''
