# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Unit F take-home assignment

def invoice(unitPrice, quantity, shipping = 10, handling = 5):
	print (f'Cost (unitPrice x quantity) = {unitPrice * quantity}')
	print (f'Shipping = {shipping}')
	print (f'Handling = {handling}') 
	print (f'Total = {(unitPrice * quantity) + shipping + handling}\n')

def printGroupMembers(groupName, *members):
	print(f'Members of {groupName}')
	for name in members:
		print (f'{name}')

def buildBell(rows):
    l1 = [[1]]
    for i in range(1, rows):
        l2 = []
        l2.append(l1[i-1][len(l1)-1])
        for j in range(0, i):
            l2.append(l1[i-1][j] + l2[j])   
        l1.append(l2)
    return l1

def printBell(lst):
	print('\n'.join(' '.join(map(str,sl)) for sl in lst))


def main():
	invoice(unitPrice = 20, quantity = 4, shipping = 8)
	invoice(unitPrice = 15, quantity = 3, handling = 15)

	printGroupMembers("Group A", "Li", "Audry", "Jia")
	groupB = ["Group B", "Sasha", "Migel", "Tanya", "Hiroto"]
	printGroupMembers(groupB[0], groupB[1], groupB[2], groupB[3], groupB[4])

	printBell(buildBell(8))

if __name__ == '__main__':
    main()

'''
Execution results:
'''
