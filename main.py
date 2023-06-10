import os

# A simple calculator

def main():
    while True:
        print("Welcome to Calculator")
        choice = input("Press \n 1 to Add \n 2 to Sub \n 3 to Multiple \n 4 to divide \n :")
        num1 = input("Enter first no : ")
        num2 = input("Enter second no : ")
        match float(choice):
            case 1:
                add(num1, num2)
            case 2:
                sub(num1, num2)
            case 3:
                multi(num1, num2)
            case 4:
                divid(num1, num2)
            case _:
                print("Invalid Option")
        
        loop_check = input("Press 1 to Try Again : ")
        os.system('cls')
        if(int(loop_check) != 1):
            break


            
def add(num1,num2):
    result = float(num1) + float(num2)
    print("Result is " , result)


def sub(num1,num2):
    result = float(num1) - float(num2)
    print("Result is " , result)

def multi(num1,num2):
    result = float(num1) * float(num2)
    print("Result is " , result)

def divid(num1,num2):
    result = float(num1) / float(num2)
    print("Result is " , result)


main()