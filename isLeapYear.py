def checkIfLeapYear(enteredYear):
    if enteredYear % 4 == 0:
        isLeap = 'is a lear year'

    if enteredYear % 100 == 0:
        isLeap = 'is not a lear year'
        
    if enteredYear % 400 == 0:
        isLeap = 'is a lear year'
    return isLeap

enteredYear = int(input('Enter in a year to see if the year is a leap year.'))

isLeap = checkIfLeapYear(enteredYear)

print(f'{enteredYear}, {isLeap}.')