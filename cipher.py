import os
print("Welcome to the Caesar Cipher Encoder/Decoder!")

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def cipher(text, shift, direction):
    cipher = ""
    for letter in text:
        if letter in alphabets:
            position = alphabets.index(letter)
            if direction == "encode":
                newposition = (position + shift) % 26
            elif direction == "decode":
                newposition = (position - shift) % 26
            else:
                print("Invalid direction! Please choose 'encode' or 'decode'.")
                return "Error"
            cipher += alphabets[newposition]
        else:
            cipher += "-"

    return cipher


wants_to_continue = True
while wants_to_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").upper()
    shift = int(input("Type the shift number:\n"))
    result = cipher(text, shift, direction)
    print(f"The {direction} text is: {result}")
    choice = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if choice == "no":
        wants_to_continue = False
        print("Goodbye!")
    else:
        os.system('cls')
