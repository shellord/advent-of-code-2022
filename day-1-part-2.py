FILE_PATH = "inputs/day-1.txt"

input_file = open("./inputs/day-1.txt", "r")


calory_list = input_file.read().split('\n\n')

for i in range(len(calory_list)):
    calory_list[i] = calory_list[i].split('\n')


sum_calories_list = []

for i in range(len(calory_list)):
    _sum = 0
    for j in range(len(calory_list[i])):
        _sum = _sum + int(calory_list[i][j])
    sum_calories_list.append(_sum)


sum_calories_list.sort()
print(sum(sum_calories_list[-3:]))
