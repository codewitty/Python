# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# In-Class Assignment H

# Second Script - Operator Overloading

class BritCoins:
	__coinValues = {"pound":240, "shilling":12, "penny":1}

	def __init__(self, **kwargs):
		self.totalPennies = 0
		if 'pound' in kwargs:
			self.totalPennies += (kwargs.get('pound') * BritCoins.__coinValues.get('pound'))
		if 'shilling' in kwargs:
			self.totalPennies += (kwargs.get('shilling') * BritCoins.__coinValues.get('shilling'))
		if 'penny' in kwargs:
			self.totalPennies += (kwargs.get('penny') * BritCoins.__coinValues.get('penny'))

	def __add__(self, other):
		total = self.totalPennies + other.totalPennies
		return BritCoins(**{"penny" : total})
		
	def __sub__(self, other):
		total = self.totalPennies - other.totalPennies
		return BritCoins(**{"penny" : total})

	def __str__(self):
		self.p = self.totalPennies // BritCoins.__coinValues.get('pound')
		self.s = (self.totalPennies % BritCoins.__coinValues.get('pound')) // BritCoins.__coinValues.get('shilling')
		self.pe = self.totalPennies - (self.p * BritCoins.__coinValues.get('pound') + self.s *  BritCoins.__coinValues.get('shilling'))
		return '{self.p} pounds {self.s} shillings {self.pe} pennies'.format(self=self)


def main():
	c1 = BritCoins(**{"pound": 4, "shilling": 24, "penny": 3})
	c2 = BritCoins(**{"pound": 3, "shilling": 4, "penny": 5})
	c3 = c1 + c2
	c4 = c1 - c2

	print(c1)
	print(c2)
	print(c3)
	print(c4)


if __name__ == '__main__':
    main()

'''
Execution Results:

5 pounds 4 shillings 3 pennies
3 pounds 4 shillings 5 pennies
8 pounds 8 shillings 8 pennies
1 pounds 19 shillings 10 pennies

'''
