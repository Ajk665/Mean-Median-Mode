import random
import statistics

diceresult = []
for i in range(0,1000):
    dice1 = random.randit(1,6)
    dice2 = random.randit(1,6)
    diceresult.append(dice1 + dice2)
mean = sum(diceresult) / len(diceresult)
standarddeviation = statistics.stdev(diceresult)
print(mean)
print(standarddeviation)