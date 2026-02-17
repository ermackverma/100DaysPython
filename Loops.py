# # for loops

# score = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 750, 65, 25, 20, 15, 5]

# max_score = 0
# summ = 0

# for i in score:
#     summ += i
#     if i > max_score:
#         max_score = i


# print(f"The highest score is {max_score} and {summ} is the total score")
# print(str(max(score)) + " and " + str(sum(score)))


# Range function --- runs from the first to the last - 1
# total = 0
# for i in range(1, 101, 2):
#     total += i

# print(total)


# Pypassowrd Generator
import random
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# numbers = '0123456789'
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = '!@#$%^&*()_+'
password = []
for i in range(4):
    password.append(random.choice(letters))
for i in range(4):
    password.append(random.choice(numbers))
for i in range(4):
    password.append(random.choice(symbols))

passs = ''
for i in password:
    passs += i
print(f'normal password:\n{passs}')

hardpass = ''
random.shuffle(password)
# print(type(newpassword))
for i in password:
    hardpass += i
print(f'hard password :\n{hardpass}')
