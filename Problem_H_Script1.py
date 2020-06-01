# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# In-Class Assignment H

# First Script - Variable-Length Keyword Arguments - kwargs

def main():

	def overseerSystem(**kwargs):
		# Iterating over the keys of the Python kwargs dictionary
		if 'temperature' in kwargs and kwargs.get('temperature') > 500:
			print(f'Warning: temperature is {kwargs.get("temperature")}')
		if 'CO2' in kwargs and kwargs.get('CO2') > .15:
			print(f'Warning: CO2 level is {kwargs.get("CO2")}')
		if 'miscError' in kwargs: 
			print(f'Misc error #{kwargs.get("miscError")}')

	overseerSystem(**{"temperature" : 550})
	overseerSystem(**{"temperature" : 475})
	overseerSystem(**{"temperature" : 450, "miscError":404})
	overseerSystem(**{"CO2" : .18})
	overseerSystem(**{"CO2" : .2, "miscError":418})

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
