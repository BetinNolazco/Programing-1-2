# Alberto Nolazco
# Period 4
# 12/2/15

import random

compNum = random.randint(1, 101)

userNum = int(input("Guess my number between 1 and 100: "))

if userNum > compNum:
    print ("Youe guessed too high, my number was %d" %(compNum))
elif userNum < compNum:
    print ("You guessed too low, my number was %d" %(compNum))
else:
    print ("You guessed my number!!")


