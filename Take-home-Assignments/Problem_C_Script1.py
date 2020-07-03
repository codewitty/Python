# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Unit C Take-Home Assignment

# First Script - Working with List

list1 = list()

list1.extend([1,3,5])
list2 = [1, 2, 3, 4]
list3 = list1 + list2

print (f'd) list3 is: {list3}')
print (f'e) list3 contains a 3: {3 in list3}')
print (f'f) list3 contains {list3.count(3)} 3s')
print (f'h) The index of the first 3 contained in list3 is {list3.index(3)}')

print (f'h) first3 = {list3.pop(list3.index(3))}')

list4 = sorted(list3)

print (f'j) list3 is now: {list3}\nj) list4 is: {list4}')
print (f'k) Slice of list3 is: {list3[2:5]}')
print (f'l) Length of list3 is {len(list3)}')
print (f'm) The max value in list3 is {max(list3)}')

list3.sort()

print (f'n) Sorted list3 is: {list3}')

list5 = [list1,list2]
list6 = [list1[num]*list2[num] for num in range(3)]

print (f'o) list5 is: {list5}')
print (f'o) list6 is: {list6}')

print (f'p) Value 4 from list5: {list5[1][3]}')

'''
Execution results:

d) list3 is: [1, 3, 5, 1, 2, 3, 4]
e) list3 contains a 3: True
f) list3 contains 2 3s
h) The index of the first 3 contained in list3 is 1
h) first3 = 3
j) list3 is now: [1, 5, 1, 2, 3, 4]
j) list4 is: [1, 1, 2, 3, 4, 5]
k) Slice of list3 is: [1, 2, 3]
l) Length of list3 is 6
m) The max value in list3 is 5
n) Sorted list3 is: [1, 1, 2, 3, 4, 5]
o) list5 is: [[1, 3, 5], [1, 2, 3, 4]]
p) Value 4 from list5: 4

'''
