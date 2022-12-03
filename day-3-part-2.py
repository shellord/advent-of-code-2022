FILE_PATH = "inputs/day-3.txt"
input_file = open(FILE_PATH, "r")


def is_small_letter(letter):
    return ord(letter) >= 97 and ord(letter) <= 122


def priority_of_letter(letter):
    if(is_small_letter(letter)):
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26


def find_repeating_letter(string_one, string_two, string_three):
    for i in string_one:
        if i in string_two and i in string_three:
            return priority_of_letter(i)


input_file_list = input_file.read().split('\n')

sum_of_priorities = 0
i = 0
j = 3

while(j != len(input_file_list)+3):
    three_strings = input_file_list[i:j]
    sum_of_priorities += find_repeating_letter(
        three_strings[0], three_strings[1], three_strings[2])
    i += 3
    j += 3

print(sum_of_priorities)
