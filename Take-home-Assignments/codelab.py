total = 0
hourlyRate = 0
hours = 0

outerLoop = int(input("Enter total employess:"))

for i in range(0, outerLoop):
	hourlyRate = int(input("Enter hourly rate:"))
	for i in range(0, 5):
		hours = int(input("Enter hours for day:"))
		total += hourlyRate * hours
print (f'Total is: {total}')
