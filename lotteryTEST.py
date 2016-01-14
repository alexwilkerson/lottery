import random
import sys

def compareNumbers(numberList1, numberList2):
    numberList1.sort()
    numberList2.sort()
    if numberList1 == numberList2:
        return True
    else:
        return False

def pickNumbers():
    return [random.randrange(1,50), random.randrange(1,50), random.randrange(1,50)]

ourPick = pickNumbers()
print ourPick

guesses = 1
while True:
    if compareNumbers(ourPick, pickNumbers()) == True: 
        print "It took " + str(guesses) + " tries to get a match."
        break
    sys.stdout.write('%d\r' % guesses)
    sys.stdout.flush()
    guesses += 1
