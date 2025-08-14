'''
author: Chris
date: 15/08/25
version: 1.0
description: This is battle code
'''
#----libraries------------
import random #lets you use randint and shuffle, along with other random modules

#---functions-------------


#---main-----------
if __name__ == '__main__':
    
    hp = 100 #our hitpoints
    dff = 13 #our defence

    en_hp = 100 #enemys hitpoints
    en_dff = 13 #enemys defence

    while(hp > 0 and en_hp > 0):
        #This loop checks that the user has entered a valid input - a, s, or h.
        while(True):
            try:
                attack = input('Please enter your attack [s]word [a]xe [h]eal: ') #makes the user enter something
                if(attack[0].lower() == 'a' or attack[0].lower == 's' or attack[0].lower() == 'h'): #checks that they entered a valid option
                    print('test')
                    break
            except:
                    print('This is not a valid input, please enter a, s, or h') #makes them try again if they entered something invalid
                    continue

        if(attack == 's'): #if they chose sword, this runs sword
            print('sword')
            pass
        elif(attack == 'a'): #If they chose axe, this runs axe
            pass
        elif(attack == 'h'): #If they chose heal, this runs heal
            pass