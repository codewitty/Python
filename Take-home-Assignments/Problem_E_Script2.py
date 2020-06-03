# Joshua Nelson Gomes (Joshua)
# CIS 41A Spring 2020
# Unit E take-home assignment

import random

# Script 2 - Guessing Game 

#this generates a random int from 1-100, inclusive
secretNum = random.randint(1,100)

print (f'Welcome to the guessing game.\nYou need to guess a number from 1 to 100.')
num = int(input('What is your guess? '))
count = 1

while num != secretNum:
	if num > secretNum:
		print (f'Guess is too high.')
	else:
		print (f'Guess is too low.')
	num = int(input('What is your guess? '))
	count+=1

print (f'Congratulations!\nYou guessed the secret number in {count} guesses!')



'''
Execution results:

Welcome to the guessing game.
You need to guess a number from 1 to 100.
What is your guess? 50
Guess is too high.
What is your guess? 25
Guess is too high.
What is your guess? 12
Guess is too high.
What is your guess? 6
Guess is too high.
What is your guess? 3
Guess is too low.
What is your guess? 4
Guess is too low.
What is your guess? 5
Congratulations!
You guessed the secret number in 7 guesses!

'''
