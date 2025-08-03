'''

'''
import random
number = random.randint(1, 10)
print('test', number)
while(True):
    guess = input('Please guess a number')
    if guess == number:
        print('You got it!')
        break
    if guess > number:
        print('You guessed too high, try again: ')
        continue
    if guess < number:
        print('You guessed too low, try again: ')
        continue
    