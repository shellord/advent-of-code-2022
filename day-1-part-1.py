FILE_PATH = "inputs/day-1.txt"

input_file = open("./inputs/day-1.txt", "r")

calories_list = []
reindeer = 1
calories = 0

highest_calories = 0

for line in input_file:
    if(line == '\n'):
        if(calories > highest_calories):
            highest_calories = calories
        reindeer += 1
        calories = 0
        continue
    calories += int(line)


print(highest_calories)
