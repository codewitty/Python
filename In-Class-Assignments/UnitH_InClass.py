# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# In-Class Assignment H

def main():

# Part One

	class StateData:
		def __init__(self, name, abbreviation, population, region):
			self.name = name
			self.abbreviation = abbreviation
			self.population = population
			self.region = region
		def __str__(self):
			return '{self.name}'.format(self=self)
		def displayState(self):
			print(f'{self.name} ({self.abbreviation}) is in the {self.region} region and has population of {self.population}')
	
	s1 = StateData("California", "CA", 39250000, "West")

	print(s1)
	s1.displayState()

# Part Two

	class StateData2:
		def __init__(self, name):
			self.name = name
		def setRegion(self, region):
			self.region = region 
		
		def getRegion(self):
			return self.region
	s2 = StateData2("California")
	s2.setRegion("West")
	s2.pop = 39250000

	print(f'{s2.name}')
	print(f'{s2.getRegion()}')
	print(f'{s2.region}')
	print(f'{s2.pop}')

# Part Three

	class StateData2:
		def __init__(self):
			self.public = "Public"
			self._protected = "Protected"
			self.__private = "Private"
	test = StateData2()
	print(f'{test.public}')
	print(f'{test._protected}')
	print(f'{test.__private}')


if __name__ == '__main__':
    main()

'''
Execution Results:

California
California (CA) is in the West region and has population of 39250000
California
West
West
39250000
Public
Protected
Traceback (most recent call last):
  File "UnitH_InClass.py", line 58, in <module>
    main()
  File "UnitH_InClass.py", line 54, in main
    print(f'{test.__private}')
AttributeError: 'StateData2' object has no attribute '__private'

shell returned 1

'''
