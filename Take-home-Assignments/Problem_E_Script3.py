# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Unit E take-home assignment Script 3

# Script 3 - Part One – Looping with String Methods

quote = "Believe you can and you're halfway there."
count = 0

for elem in quote:
	if elem == 'a':
		print (f' a found at index {count}')
	count+=1

# Part 2 - Nested Loops

num = int(input('Please enter the number of rows for the multiplication table: '))

for i in range(1, num + 1): 
	for j in range (1, i + 1):
		print (f'{i * j:>5}', end = "")
	print ("\n")


'''
Execution results:

a found at index 13
 a found at index 16
 a found at index 28
 a found at index 32
Please enter the number of rows for the multiplication table: 12
    1

    2    4

    3    6    9

    4    8   12   16

    5   10   15   20   25

    6   12   18   24   30   36

    7   14   21   28   35   42   49

    8   16   24   32   40   48   56   64

    9   18   27   36   45   54   63   72   81

   10   20   30   40   50   60   70   80   90  100

   11   22   33   44   55   66   77   88   99  110  121

   12   24   36   48   60   72   84   96  108  120  132  144

'''
