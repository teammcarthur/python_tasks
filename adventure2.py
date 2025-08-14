'''
author: Chris
date: 15/08/25
version: 1.0
description: This is battle code
'''
#----libraries------------
import random
import time

#---functions-------------
def letterinputs():
    letterlist = []
    while(True):
        while(True):
            letter = input('Please enter a letter: ')
            if(len(letter) < 2 and letter.isalpha):
                break
            else: 
                print('Please enter a single letter')
                continue

        letterlist.append(letter) #This code adds the most recently entered letter into a list for later use
        print('Letter is being stored, please wait...')
        time.sleep(2) #This pauses the code for 2 seconds
        print('...')
        time.sleep(2) #This pauses the code for 2 seconds
        print('...')
        print(f'{letter} has been stored')
        continue


#---main-----------
if __name__ == '__main__':
    hp = 100
    dff = 13

    en_hp = 100
    en_dff = 13
    letterinputs()