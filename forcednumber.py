
while True:
    age = input('Enter your age: ')
    if age.isnumeric() and age > 12 and age < 18:
        print('age accepted')
        ageint = int(age)
        break
    else:
        print('This is an invalid age, please try again: ')
        continue
print(age)
print(ageint)
print(type(ageint))
print(type(age))












'''
age = 0

age = int(input('Enter your age: '))

print(age)
'''







age = 0
while(True):
    try:

        age = int(input('Enter your age: '))
        

    except:
        print('Error happened')
        continue
    if( age >= 12 and age <= 18):
        break

print(age)
