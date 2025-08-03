'''

'''

#---Libraries---
#import random
from random import shuffle
from random import choice


#---Main Program---
sports = ['Football', 'Rugby', 'Hockey', 'Basketball', 'Cricket', 'Volleyball']

sports.append('Tennis')

print(sports)
shuffle(sports) #or random.shuffle if importted the regular way?????
print(sports)

random_sport = choice(sports)
print(random_sport)
