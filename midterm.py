x = (1,2,3, 3, 2, 1)

c = {1, 2, 3}

d = [1, 1, 3, 4, 4]

t = {'a': 1, 'b': 2, 'c': 3}

for i in range(5, 3, -1):
	print(i)
for i in range( 3):
	print(i)
for i in range(2, 4):
	print(i)

class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"}
class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"}
class3 = {"Migel", "Zhang", "Hiroto", "Anita", "Jia"}



y = (class1.intersection(class2)) - class3

print(y)


print(x)
print(c)
print(d)
print(t)
print(f'{42 in d}')
for i in range(2, 21, 2):
	print(i)


def priceGuide(avgPrice):
	if avgPrice <= 10:
		print (f'Inexpensive')
	if avgPrice > 10 and avgPrice <= 30:
		print (f'Moderate')
	if avgPrice > 30:
		print (f'Pricey')

priceGuide(54)
priceGuide(1)
priceGuide(454)
priceGuide(30)







































