# # who will pay the bill

# import random
# friends = ["Mayank", "Deepti", "Neha", "Papa", "Mummy", "Jiju"]
# print("1st person", random.choice(friends))
# print("2nd person", friends[random.randint(0, 5)])


# Rock Paper Scissors
# Rock
import random
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player = int(input(
    "What do you want to choose? 1 for ROCK, 2 for PAPER, 3 for SCISSORS : "))
compchoice = [1, 2, 3]
computer = random.choice(compchoice)


if player == 1:
    if computer == 1:
        print("Your choice:\n Rock")
        print(Rock)
        print("Computer choice:\n Rock")
        print(Rock)
        print("\n ----DRAW----")
    elif computer == 2:
        print("Your choice:\n Rock")
        print(Rock)
        print("Computer choice:\n Paper")
        print(Paper)
        print("\n ----***COMPUTER WON***----")
    elif computer == 3:
        print("Your choice:\n Rock")
        print(Rock)
        print("Computer choice:\n Scissors")
        print(Scissors)
        print("\n ----***PLAYER WON***----")

if player == 2:
    if computer == 2:
        print("Your choice:\n Paper")
        print(Paper)
        print("Computer choice:\n Paper")
        print(Paper)
        print("\n ----DRAW----")
    elif computer == 3:
        print("Your choice:\n Paper")
        print(Paper)
        print("Computer choice:\n Scissors")
        print(Scissors)
        print("\n ----***COMPUTER WON***----")
    elif computer == 1:
        print("Your choice:\n Paper")
        print(Paper)
        print("Computer choice:\n Rock")
        print(Rock)
        print("\n ----***PLAYER WON***----")

if player == 3:
    if computer == 3:
        print("Your choice:\n Scissors")
        print(Scissors)
        print("Computer choice:\n Scissors")
        print(Scissors)
        print("\n ----DRAW----")
    elif computer == 1:
        print("Your choice:\n Scissors")
        print(Scissors)
        print("Computer choice:\n Rock")
        print(Rock)
        print("\n ----***COMPUTER WON***----")
    elif computer == 2:
        print("Your choice:\n Scissors")
        print(Scissors)
        print("Computer choice:\n Paper")
        print(Paper)
        print("\n ----***PLAYER WON***----")
