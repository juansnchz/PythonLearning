import random

def rollDice(numberOfDice: int):
    """Returns the sum of random roll of the given number of six-sided dice"""
    sumOfDice = 0
    rolledDice = []
    for i in range(numberOfDice):
        rollednumber = random.randint(1,6)
        sumOfDice+= rollednumber
        rolledDice.append(rollednumber)

    return sumOfDice, rolledDice

print(rollDice(3))
