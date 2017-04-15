#!/usr/bin/env python

from random import randint
import time

count = 0
while (count < 9):
    x = randint(0,14)
    print("Your pH level is")
    print(x)
    if x >= 0 and x <= 2:
        print("Alert! Your pH levels are critically low. Water may be contaminated.")
    elif x > 2 and x <= 5:
        print("Your pH levels are low. Recommend checking filters.")
    elif x > 9 and x <= 11:
        print("Your ph levels are high. Recommend checking filters.")
    elif x > 11 and x <=14:
        print("Alert! Your ph levels are high. Take caution, water may be contaminated.")
    else:
        print("Your pH levels are stable.")

    time.sleep(60)