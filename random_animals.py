import random

# List of animal names
animals = [
    "Lion", "Tiger", "Elephant", "Giraffe", "Zebra", "Monkey", "Rabbit",
    "Dog", "Cat", "Horse", "Cow", "Pig", "Chicken", "Duck", "Goat",
    "Sheep", "Bear", "Wolf", "Fox", "Deer", "Snake", "Lizard", "Frog",
    "Fish", "Shark", "Whale", "Dolphin", "Penguin", "Eagle", "Parrot",
    "Crow", "Sparrow", "Peacock", "Owl", "Bat", "Mouse", "Rat",
    "Squirrel", "Chipmunk", "Beaver", "Otter", "Badger", "Hedgehog"
]


def get_random_animals(num):
    """
    Takes a number and returns that many random animal names.

    Args:
        num: The number of random animal names to return

    Returns:
        A list of random animal names
    """
    if num <= 0:
        return []
    else:
        # If requested more than available, allow repetitions
        # Otherwise, use random.sample for unique selection
        if num > len(animals):
            result = []
            for i in range(num):
                result.append(random.choice(animals))
            return result
        else:
            return random.sample(animals, num)


# Main program
if __name__ == "__main__":
    try:
        # Get user input
        user_input = input("Enter a number: ")
        number = int(user_input)

        # Get random animals
        random_animals = get_random_animals(number)

        # Display results
        print(f"\nHere are {len(random_animals)} random animal names:")
        for i, animal in enumerate(random_animals, 1):
            print(f"{i}. {animal}")

    except ValueError:
        print("Please enter a valid integer!")
