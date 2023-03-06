def commaFormat(number):

    numPart = str(number)
    decimalPart = ""
    finalString = ""

    if "." in numPart:
        decimalPart = numPart[numPart.index("."):]
        numPart = numPart[:numPart.index(".")]

    while len(numPart)>2:
        threeDigits = numPart[-3:len(numPart)]
        numPart = numPart[:-3]
        finalString = "," + threeDigits + finalString

    if len(numPart) == 0:
        finalString = finalString[1:]
    else:
        finalString = numPart + finalString

    return finalString + decimalPart




assert commaFormat(1) == '1'
assert commaFormat(10) == '10'
assert commaFormat(100) == '100'
assert commaFormat(1000) == '1,000'
assert commaFormat(10000) == '10,000'
assert commaFormat(100000) == '100,000'
assert commaFormat(1000000) == '1,000,000'
assert commaFormat(1234567890) == '1,234,567,890'
assert commaFormat(1000.123456) == '1,000.123456'


print(commaFormat(9289230944234625827339214866723981498190))