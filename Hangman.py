import random
from General import animals
# word_list = ["Mouse", "Lion", "Tiger", "Elephant", "Zebra", "Monkey", "Panda"]

print("*****Welcome to Hangman Game!*****")

stages = ['KILLED', 'KILLE', 'KILL', 'KIL', 'KI', 'K', '']
chosen_word = random.choice(animals).lower()
# print(chosen_word)

# no. of blank placeholders first
placeholder = ""
for i in chosen_word:
    placeholder += "_"

print(placeholder)

# no. of lives
lives = 6


# word_len = len(chosen_word)
game_over = False

check_list = []
already_guessed = []
while not game_over:
    print(f"You have {lives} lives left.")
    guess = input("Guess the word: ").lower()
    # if the user already guessed this letter, skip processing
    if guess in already_guessed:
        print(f"You guessed {guess}, that's already guessed.")
        print(stages[lives])
        continue

    already_guessed.append(guess)

    display = ""
    for char in chosen_word:
        if char == guess:
            display += char
            if char not in check_list:
                check_list.append(char)
        elif char in check_list:
            display += char
        else:
            display += "-"

    print(display)

    if display == chosen_word:
        game_over = True
        print("You win!")

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print("You lose!... The word was " + chosen_word)

    print(stages[lives])
