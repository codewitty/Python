# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Unit E take-home assignment

# Script 3 - Part One – Looping with String Methods

quote = "Believe you can and you're halfway there."
count = 0

for elem in quote:
	if elem == 'a':
		print (f' a found at index {count}')
	count+=1

# Part 2 - Nested Loops

num = int(input('Please enter the number of rows for the multiplication table: '))
mul = 1

for (int i = 0; i < num; ++i) {
	for (int j = i + 1; j >= i + 2; j++) {
		cout << j * mul << " " ;
		mul++;
	}
	cout << "\n";
}










'''
Execution results:

'''
