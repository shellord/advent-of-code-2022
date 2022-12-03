FILE_PATH = "inputs/day-3.txt"
input_file = open(FILE_PATH, "r")


def is_small_letter(letter):
    return ord(letter) >= 97 and ord(letter) <= 122


def priority_of_letter(letter):
    if(is_small_letter(letter)):
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26


def find_repeating_letter(string_one, string_two):
    for i in string_one:
        if i in string_two:
            return priority_of_letter(i)


sum_of_priorities = 0

for i in input_file:
    sum_of_priorities += find_repeating_letter(i[:len(i)//2], i[len(i)//2:])

print(sum_of_priorities)
