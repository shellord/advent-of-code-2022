FILE_PATH = "inputs/day-2.txt"
input_file = open("./inputs/day-2.txt", "r")


rounds = input_file.read().split('\n')

scores = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

mappings = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'loss',
    'Y': 'draw',
    'Z': 'win'
}


def get_score(round):
    oponent_move = round.split(' ')[0]
    what_should_i_do = round.split(' ')[1]

    if mappings[what_should_i_do] == 'win':
        if(mappings[oponent_move] == 'rock'):
            return scores['paper'] + 6
        elif(mappings[oponent_move] == 'paper'):
            return scores['scissors'] + 6
        elif(mappings[oponent_move] == 'scissors'):
            return scores['rock'] + 6

    elif mappings[what_should_i_do] == 'draw':
        return 3 + scores[mappings[oponent_move]]

    elif mappings[what_should_i_do] == 'loss':
        if(mappings[oponent_move] == 'rock'):
            return scores['scissors']
        elif(mappings[oponent_move] == 'paper'):
            return scores['rock']
        elif(mappings[oponent_move] == 'scissors'):
            return scores['paper']


total_score = 0
for i in rounds:
    total_score += get_score(i)


print(total_score)
