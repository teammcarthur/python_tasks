import random
import string

#----functions----
def main():
    name = input('Enter your name: ') #string
    while(True):
        age = input('Enter your age: ')
        if age.isnumeric:
            break
        else:
            print('This is not a valid age, please try again.')
            continue
    ageint = int(age)
    if name == 'Chris':
        print(f'Welcome {name} to our program')
    for years in range(ageint):
        print(f'You are {age} years old')

    info = []
    info.append(name)
    info.append(age)

    for i in info:
        print(i)

#-------main-------

if(__name__ == '__main__'):
    main()