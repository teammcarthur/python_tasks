'''
Author: Chris
Version: 1.0
Date: 
Description: This is a number guessing game
'''
def guessing():
    import random
    while(True):
        name = input('Please enter your name: ')
        if(len(name) >=2 and len(name) <= 20 and name.isalpha):
                break
        else:
                print('This is an invalid name')
                continue
    number = random.randint(1, 10)
    numberint = int(number)
    guesses = 0
    #print('the number is', numberint)
    while(True):
        while(True):
            guess = input('Please guess a number: ')
            if guess.isnumeric():
                    break
            else:
                print('This guess is invalid')
                continue
        guessint = int(guess)
        guesses = guesses + 1
        if guessint == numberint:
            print('You got it!')
            break
        if guessint > numberint:
            print('You guessed too high, try again: ')
            continue
        if guessint < numberint:
            print('You guessed too low, try again: ')
            continue
    print(f'You guessed {guesses} times!')

#-----main program------
if __name__ == '__main__':
    guessing()