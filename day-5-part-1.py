FILE_PATH = "inputs/day-5.txt"
input_file = open(FILE_PATH, "r")

stack = [[] for i in range(9)]


def make_stacks(input_file):
    item_pos = 0

    for line in input_file:
        offset = 0
        if('1' in line):
            break
        row = line.split(' ')

        for i in range(len(row)):
            char = row[i]
            if ((char != '') and (char != '\n')):
                item_pos = i+offset
                crate_pos = item_pos//4 + 1
                stack[crate_pos-1].append(char[1])
                offset += 3

        item_pos += 1

    for i in stack:
        i.reverse()


def move_crate(count, source, destination):
    for _ in range(count):
        crate = stack[source].pop()
        stack[destination].append(crate)


def perform_moves():
    for line in input_file:
        if('move' not in line):
            continue
        command = line.split(' ')
        count = int(command[1])
        source = int(command[3]) - 1
        destination = int(command[5][0]) - 1
        move_crate(count, source, destination)


def get_last_crates():
    last_crates = []
    for i in stack:
        last_item = i.pop()
        last_crates.append(last_item)
    return ''.join(last_crates)


make_stacks(input_file)
perform_moves()
print(get_last_crates())
