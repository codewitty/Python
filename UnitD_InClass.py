# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# In-Class Assignment B

# String methods

name = input('Whats your name?\n')

print(name.upper())

print("Length: ", len(name))

print("Fourth letter of your name: ", name[3])

name2 = name.replace('o', 'x')

print("New Name: ", name2)

print("Original Name: " , name)

# Counting and Finding

quote = "Believe you can and you're halfway there."

print("'a' Count: ", quote.count('a'))

print("Index of all the \"a\" characters")
index = quote.find('a')
print(index)
index = quote.find('a', index+1)
print(index)
index = quote.find('a', index+1)
print(index)
index = quote.find('a', index+1)
print(index)

'''
Output:

Whats your name?
George Washington
GEORGE WASHINGTON
Length:  17
Fourth letter of your name:  r
New Name:  Gexrge Washingtxn
Original Name:  George Washington
'a' Count:  4
Index of all the "a" characters
13
16
28
32
'''
