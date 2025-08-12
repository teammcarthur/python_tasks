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
    answer = num1-num2
#multiplication function
def multiplication():
    answer = num1*num2
#division function
def division():
    answer = num1/num2


def main():
    if __name__ == '__main__': 
        while(True):
            num1 = int(input('Enter a number'))
            num2 = int(input('Enter a number'))
            op = input('Enter you operation (+, -, *, /): ')
            if(op == '+'):
                addition(num1, num2) = answer
                print(f"{num1}+{num2}=={answer}")
                break
            elif(op == '-'):
                subtraction(num1, num2)
                print(f"{num1}-{num2}=={answer}")
                break
            elif(op == '*'):
                multiplication(num1, num2)
                print(f"{num1}*{num2}=={answer}")
                break
            else:
                if(num1 or num2 == 0):
                    print('You cannot do this calculation')
                    continue
                else:
                    division(num1, num2)
                    print(f"{num1}/{num2}=={answer}")
                    break
main()
