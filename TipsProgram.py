print("Welcome to the tip calculator!")
tbill = float(input("What was the total bill? $ "))
tip = int(input("How % tip would you like to give? 0 10 12 15 "))
people = int(input("How many people to split the bill? "))

perperson = round((tbill * (1 + (tip/100)))/people, 2)

print(f"Each person should pay: $ {perperson}")
