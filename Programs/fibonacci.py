def userInput():
    number = int(input('Please enter the number between 1 - 40 to find out the fibonacci :'))
    return number

def findFibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return findFibonacci(number - 1) + findFibonacci (number - 2)


def main():
    userNumber = userInput()
    print(findFibonacci(userNumber))

main()

