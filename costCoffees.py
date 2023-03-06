def getCostOfCoffee(numberOfCoffees,pricePerCoffee):
    accumulatedCost = 0
    countedCoffees = 1
    while countedCoffees <= numberOfCoffees:
        accumulatedCost += pricePerCoffee
        countedCoffees += 1

        if countedCoffees % 9 == 0:
            countedCoffees +=1
    return accumulatedCost



assert getCostOfCoffee(7, 2.50) == 17.50
assert getCostOfCoffee(8, 2.50) == 20
assert getCostOfCoffee(9, 2.50) == 20
assert getCostOfCoffee(10, 2.50) == 22.50

for i in range(1, 4):
    assert getCostOfCoffee(0, i) == 0
    assert getCostOfCoffee(8, i) == 8 * i
    assert getCostOfCoffee(9, i) == 8 * i
    assert getCostOfCoffee(18, i) == 16 * i
    assert getCostOfCoffee(19, i) == 17 * i
    assert getCostOfCoffee(30, i) == 27 * i

#Another solution that is more efficient


def getCostCoffees(numCoffees, priceXCoffee):
    freeCoffees =numCoffees // 9
    paidCoffees = numCoffees - freeCoffees

    return paidCoffees * priceXCoffee


print(getCostCoffees(1000000000, 2.50))