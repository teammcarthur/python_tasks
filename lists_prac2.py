'''
Author: Chris McArthur
Date: 5/08/25
Version: 1.0
Description: 
'''
import random
from random import shuffle

#-----functions---------
def lottery():
    names_list = ['Greg', 'Bob', 'Jenna', 'Tim', 'Jimmy']
    random_number = random.randint(0, len(names_list))
    print(f'The random number is {random_number}')
    print(f'The lucky winner is {names_list[random_number]}')


students_list = ['Greg', 'Bob', 'Jenna', 'Tim', 'Jimmy']
print(students_list[0])
print(students_list[1])
print(students_list[2])
print(students_list[3])
print(students_list[4])

for student in students_list:
    print(student)


count = 0
while count < len(students_list):
    print(count+1, students_list[count])
    count+=1
print(f'That is every student, there are {count} of them.')

students_list.append('Jake')
students_list.append('Jack')
students_list.append('James')
shuffled_list = shuffle(students_list) #using a shuffled list
print(shuffled_list)


#Using a random number to access the list
number = random.randint(0, len(students_list))
print(students_list[number])

new_students = []
while(True):
    entry = input('Please enter the name of any new student, or enter none, if there are no new students to be entered')
    if entry != 'none':
        new_students.append(entry)
    else:
        print('finished entering names')
        break
print('These are all the new students: ',new_students)

#-----main-----
if (__name__ == '__main__'):
    lottery()