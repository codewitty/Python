# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Unit E take-home assignment

# Script 1 - Decision Making

name = input('Please enter the plant name: ')
plant_type = input('Please enter the plant type: ')
plant_height = int(input('Please enter the plant height: '))

if plant_type == 'Vegetable':
	print(f' A {name} can be planted in the Vegetable Garden')

elif plant_type == 'Flower' and 6 >= plant_height and plant_height > 3:
	print(f' A {name} can be planted in the High Garden')
	
elif plant_type == 'Flower' and 3 >= plant_height:
	print(f' A {name} can be planted in the Low Garden or the High Garden')

else:
	print (f' A {name} cannot be planted in any Garden')


'''
Execution results:

Please enter the plant name: Lily
Please enter the plant type: Flower
Please enter the plant height: 3
 A Lily can be planted in the Low Garden or the High Garden

Press ENTER or type command to continue
Please enter the plant name: Bonsai
Please enter the plant type: Tree
Please enter the plant height: 2
 A Bonsai cannot be planted in any Garden

Please enter the plant name: Carrots
Please enter the plant type: Vegetable
Please enter the plant height: 1
 A Carrots can be planted in the Vegetable Garden

Please enter the plant name: Corn
Please enter the plant type: Vegetable
Please enter the plant height: 8
 A Corn can be planted in the Vegetable Garden

Please enter the plant name: Rose
Please enter the plant type: Flower
Please enter the plant height: 5
 A Rose can be planted in the High Garden

Please enter the plant name: Sunflower
Please enter the plant type: Flower
Please enter the plant height: 8
 A Sunflower cannot be planted in any Garden
 '''
