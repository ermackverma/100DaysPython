
import os
print("Welcome to the Bidding Program !")

bidding_dict = {}
more = True


def bidder():
    name = input("What is your name? \n")
    bid = int(input("What is your bid? \n"))
    bidding_dict[name] = bid


while more:
    bidder()
    morebidders = input("Are there more buyers? y or n\n").lower()
    if morebidders == 'y':
        os.system('cls')

    else:
        more = False
        print("Bye")
        print("Calculating the winner...")
        resultbid = max(bidding_dict.values())
        resultname = next(k for k, v in bidding_dict.items()
                          if v == max(bidding_dict.values()))
        print(f"The winner is {resultname} with a bid of ${resultbid}")


print(bidding_dict)
