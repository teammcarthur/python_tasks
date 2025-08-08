num1 = 0
num2 = 0
op = ''
answer = 0
#----------Functions--------------------------------

#addition function
def addition():
    answer = num1+num2
#subtraction function
def subtraction():
    pass
#multiplication function

#division function


def main():
    if __name__ == '__main__': 

        num1 = int(input('Enter a number'))
        num2 = int(input('Enter a number'))
        op = input('Enter you operation (+, -, *, /): ')
        if(op == '+'):
            addition(num1, num2) = answer
            print(f"{num1}+{num2}=={answer}")
        elif(op == '-'):
            subtraction(num1, num2)
        elif(op == '*'):
            pass
        else:
            pass
main()
