count = 0
inputNum = 1
prevInput = -1

while (inputNum > 0):
	inputNum = int(input())
	if inputNum == prevInput:
		count += 1
	prevInput = inputNum
		
print (f'{count}')
