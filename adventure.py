'''
author: Chris
date: 15/08/25
version: 1.0
description: This is battle code
'''
#----libraries------------


#---functions-------------


#---main-----------
if __name__ == '__main__':
    
    hp = 100 #our hitpoints
    dff = 13 #our defence

    en_hp = 100 #enemys hitpoints
    en_dff = 13 #enemys defence

    while(hp > 0 and en_hp > 0):
        attack = input('Please enter your attack [s]word [a]xe [h]eal: ')