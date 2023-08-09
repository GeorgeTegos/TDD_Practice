def fizz_buzz():
    listToAssert = []
    for number in range(1,100):
        if (number % 3 == 0) and (number % 5 == 0):
            textToPrint = 'FizzBuzz'
            print(textToPrint)
            listToAssert.append(textToPrint)
        elif number % 3 == 0:
            textToPrint = 'Fizz'
            print(textToPrint)
            listToAssert.append(textToPrint)
        elif number % 5 == 0:
            textToPrint = 'Buzz'
            print(textToPrint)
            listToAssert.append(textToPrint)
        else:
            textToPrint = number
            print(textToPrint)
            listToAssert.append(textToPrint)

    return listToAssert

fizz_buzz()