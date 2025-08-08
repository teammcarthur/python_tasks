def numbermultiplier():
    average_list = []
    temp = 0
    for i in range(5):
        while(True):
            entry = input('Enter a number: ')
            if entry.isnumeric:
                print('Number collected, please enter another')
                entryint = int(entry)
                average_list.append(entryint)
                print(average_list)
                break
            else: 
                continue
    for i in range(len(average_list)):
        temp += average_list[i]
    average = temp/len(average_list)
    print(average)

#-----main-----
if __name__ == '__main__':
    numbermultiplier()