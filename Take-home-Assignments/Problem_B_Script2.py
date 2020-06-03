# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Unit B Take-Home 

# Second Script:

# Printing a well formatted invoice

s_beads = 9.20
m_beads = 8.52
l_beads = 7.98

s_number = int(input('How many small beads would you like?\n'))
m_number = int(input('How many medium beads would you like?\n'))
l_number = int(input('How many large beads would you like?\n'))

size = 'SIZE'
qty = 'QTY'
cpb = 'COST PER BOX'
tot = 'TOTALS'

# Print invoice table
print(f'{size:15} {qty:15} {cpb:20} {tot:10}')
print (f'Small {s_number:>13} {s_beads:>24.2f} {s_beads * s_number:>14.2f}')
print (f'Medium{m_number:>13} {m_beads:>24.2f} {m_beads * m_number:>14.2f}')
print (f'Large {l_number:>13} {l_beads:>24.2f} {l_beads * l_number:>14.2f}')

'''
Execution results:

How many small beads would you like?
10
How many medium beads would you like?
9
How many large beads would you like?
8
SIZE            QTY             COST PER BOX         TOTALS
Small            10                     9.20          92.00
Medium            9                     8.52          76.68
Large             8                     7.98          63.84

How many small beads would you like?
5
How many medium beads would you like?
10
How many large beads would you like?
15
SIZE            QTY             COST PER BOX         TOTALS
Small             5                     9.20          46.00
Medium           10                     8.52          85.20
Large            15                     7.98         119.70
'''
