import random
import sys

def pickNumbers():
    numbers = []
    num = random.randrange(69) + 1
    while len(numbers) < 5:
        numbers.append(num)
        while num in numbers:
            num = random.randrange(69) + 1

    return numbers

def compareNumbers(numberList1, numberList2):
    numberList1.sort()
    numberList2.sort()
    if numberList1 == numberList2:
        return True
    else:
        return False

ourPick = pickNumbers()
ourPowerball = random.randrange(1,27)
print "The lottery numbers: " + str(ourPick) + " powerball: " + str(ourPowerball)

guesses = 1
while True:
    if compareNumbers(ourPick, pickNumbers()):
        if ourPowerball == random.randrange(1,27):
            print "It took " + str(guesses) + " tries to get a match."
            break
    sys.stdout.write(' Guesses: %d\r' % guesses)
    sys.stdout.flush()
    guesses += 1
