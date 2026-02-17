
import strings
import random

# print(random.randint(2, 20))

# print(strings.check)

# random.random
# [0,1) -- will include 0 but wont include 1

# random.uniform [0,1] -- include both 0 and 1

# Random heads or tails

# 1st way
ran = random.randint(0, 1)
if ran == 0:
    print("Heads!")
else:
    print("Tails!")

# 2nd way
ran = (random.uniform(0, 1))*10
if ran <= 5:
    print(f"Heads! {ran}")
else:
    print(f"Tails!  {ran}")
