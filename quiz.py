'''
author: Chris
version: 1.0
date: 14/08/25
description: 5 question quiz
'''


#-------functions----------------
def quiz():
    questionnum = 0
    checker = 0
    correctanswers = 0
    incorrectanswers = 0
    answerlist = []
    questions = ['Mars has 2 moons', 'Australia is the largest island', 'The Moon is larger than Mercury', 'Bats are the only mammals with wings', 'The Chameleon Run 2-4 speedrun world record is 16.064 seconds']
    quizanswers = ['T', 'F', 'F', 'F', 'T']

    #This checks that the user is entering a valid name
    while(True):
        name = input('Please enter your name: ')
        if(len(name) >= 2 and len(name) <=20 and name.isalpha):
                break
        else:
            print('This is an invalid name')
            continue

    print('Enter T or F to answer each true/false question')

    #This code is asking the user each question in order, and storing their answer to each question so the answers can be checked
    while(questionnum <= (len(questions) -1)): 
        print(questions[questionnum])
        while(True):
            #This code is checking that the user enters one of the 2 possible answers, and makes them try again if they do not
            answer = input('Enter your answer (T or F): ')
            if(answer == 'T' or answer == 'F'):
                break
            else:
                print('This is an invalid answer, please enter T or F')
                continue
        answerlist.append(answer)
        questionnum += 1
        continue

    #This code is checking whether or not the users answers are correct, and prints out a statement to tell the user how many questions they got correct
    while(True): 
        if(checker <= (len(answerlist) - 1)):
            if(answerlist[checker] == quizanswers[checker]):
                correctanswers += 1
            else:
                incorrectanswers += 1
            checker += 1
        else:
            print(f'You got {correctanswers} questions correct and {incorrectanswers} questions incorrect.')
            break

        
#----main--------------
if(__name__ == '__main__'):
    quiz()