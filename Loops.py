# for loops

score = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 750, 65, 25, 20, 15, 5]

max_score = 0
summ = 0

for i in score:
    summ += i
    if i > max_score:
        max_score = i


print(f"The highest score is {max_score} and {summ} is the total score")
print(str(max(score)) + " and " + str(sum(score)))
