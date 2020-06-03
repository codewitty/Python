# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Unit A Take-Home Assignment
#
# This program practices integer and float product/division
# and formatting output.

import math

print (f'\nBasic math and string operations')
a = pow(3, 2.5)
print(a)

b = 2
b += 3;
print(b)

c = 12
c /= 12
print(c)

d = 5 % 3
print(d)

print (f'\nBuilt-in functions abs, round, and min')
print(abs(5-7))

print(round(3.14159,4))

print(round(186282,-2))

print(min(6, -9, -3, 0))


print (f'\nFunctions from the math module')
num = float(input(f'Please enter a number\n'))

print(f'The square root of your number is {round(math.sqrt(num), 2)}')

print(f'The base 10 log of your number is {round(math.log10(num), 2)}')

print (f'\nComplex numbers')

z1 = (4 + 3j)
z2 = (2 + 2j)
z3 = z1 * z2

print (f'The value of z3 is: {z3}')

'''
Execution results:

Basic math and string operations
15.588457268119896
5
1.0
2

Built-in functions abs, round, and min
2
3.1416
186300
-9

Functions from the math module
Please enter a number
7.6
The square root of your number is 2.76
The base 10 log of your number is 0.88

Complex numbers
The value of z3 is: (2+14j)

'''
