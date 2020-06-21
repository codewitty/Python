# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Take Home Assignment J

import random

def diceGame():
	prize = 0
	a = True
	while a == True:
		dice = random.randint(1, 6)
		if (dice < 4):
			a = False
		else:
			prize += dice
	return prize

def main():
	max_prize = 0
	game = 10000
	total_prize = 0
	for i in range(0, game):
		game_prize = diceGame()
		if game_prize > max_prize:
			max_prize = game_prize
		total_prize += game_prize 
	print (f'Average amount won = {total_prize/10000:0.2f}')
	print (f'Max amount won = {max_prize}')



if __name__ == '__main__':
    main()

'''
Execution Results:

Average amount won = 4.90
Max amount won = 65

'''
