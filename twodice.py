import random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
print("your first roll was " + str(dice1) + " your second roll was " + str(dice2))
if dice1 + dice2 == 6 or dice1 + dice2 == 7 or dice1 + dice2 == 8:
    print("You Win!")
else:
    print("You Lose.")