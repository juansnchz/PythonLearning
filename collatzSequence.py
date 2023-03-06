def collatz(startingNumber):
    if startingNumber <= 0:
        return []
    sequence = [startingNumber]
    processedNumber = startingNumber


    while processedNumber != 1:
        if processedNumber % 2 == 0:
            processedNumber = processedNumber//2
            sequence.append(processedNumber)
        elif processedNumber % 2 == 1:
            processedNumber = 3*processedNumber+1
            sequence.append(processedNumber)


    if processedNumber == 1:

        return sequence


print(collatz(-256))
assert collatz(0) == []
assert collatz(10) == [10, 5, 16, 8, 4, 2, 1]
assert collatz(11) == [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
assert collatz(12) == [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]

assert len(collatz(256)) == 9
assert len(collatz(257)) == 123
import random
random.seed(42)
for i in range(1000):
    startingNum = random.randint(1, 10000)
    seq = collatz(startingNum)
    assert seq[0] == startingNum # Make sure it includes the starting number. assert seq[-1] == 1 # Make sure the last integer is 1.
