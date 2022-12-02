FILE_PATH = "inputs/day-2.txt"
input_file = open("./inputs/day-2.txt", "r")


rounds = input_file.read().split('\n')

scores = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

mappings = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}


def get_score(round):
    oponent_move = round.split(' ')[0]
    my_move = round.split(' ')[1]

    if mappings[oponent_move] == mappings[my_move]:
        return 3 + scores[my_move]
    elif (mappings[oponent_move] == 'rock' and mappings[my_move] == 'scissors') or (mappings[oponent_move] == 'paper' and mappings[my_move] == 'rock') or (mappings[oponent_move] == 'scissors' and mappings[my_move] == 'paper'):
        return 0 + scores[my_move]

    return 6 + scores[my_move]


total_score = 0
for i in rounds:
    total_score += get_score(i)

print(total_score)
