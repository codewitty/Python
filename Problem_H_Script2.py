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
		

	def __str__(self):
		return '{self.totalPennies}'.format(self=self)
	def displayState(self):
		print(f'{self.name} ({self.abbreviation}) is in the {self.region} region and has population of {self.population}')

def main():
	c1 = BritCoins(pound = 4, shilling = 3, penny = 2)

	print(c1)


if __name__ == '__main__':
    main()
'''
Execution Results:

Warning: temperature is 550
Misc error #404
Warning: CO2 level is 0.18
Warning: CO2 level is 0.2
Misc error #418

'''
