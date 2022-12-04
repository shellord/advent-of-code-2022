FILE_PATH = "inputs/day-4.txt"
input_file = open(FILE_PATH, "r")


def check_overlap(section_one, section_two):
    lower_part_of_section_one = int(section_one.split('-')[0])
    higher_part_of_section_one = int(section_one.split('-')[1])
    lower_part_of_section_two = int(section_two.split('-')[0])
    higher_part_of_section_two = int(section_two.split('-')[1])

    if((lower_part_of_section_one >= lower_part_of_section_two) and (lower_part_of_section_one <= higher_part_of_section_two)):
        return True
    elif((lower_part_of_section_two >= lower_part_of_section_one) and (lower_part_of_section_two <= higher_part_of_section_one)):
        return True


count_of_overlap_pairs = 0

for i in input_file:
    if(check_overlap(i.split(',')[0], i.split(',')[1])):
        count_of_overlap_pairs += 1

print(count_of_overlap_pairs)
