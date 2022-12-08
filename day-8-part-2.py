FILE_PATH = "inputs/day-8.txt"
data = open(FILE_PATH, 'r')


tree_list = []

for i in data:
    tree_list.append(i.strip())


no_of_tree_in_edges = len(tree_list[0]) * 4 - 4


scenic_score = 1


def find_scenic_score(row, col):
    tree = tree_list[row][col]

    # check distance to top
    distance_to_top = 0
    i = row-1
    while(i >= 0):
        distance_to_top += 1
        if(tree_list[i][col] >= tree):
            break
        i -= 1

    # check distance to bottom
    distance_to_bottom = 0
    i = row+1
    while(i < len(tree_list)):
        distance_to_bottom += 1
        if(tree_list[i][col] >= tree):
            break

        i += 1

    # check distance to right
    distance_to_right = 0
    i = col+1
    while(i <= len(tree_list[0])-1):
        distance_to_right += 1
        if(tree_list[row][i] >= tree):
            break
        i += 1

    # check distance to left
    distance_to_left = 0
    i = col-1
    while(i >= 0):
        distance_to_left += 1
        if(tree_list[row][i] >= tree):
            break
        i -= 1

    return distance_to_top * distance_to_bottom * distance_to_left * distance_to_right


highest_scenic_score = 0

for row in range(1, len(tree_list[0])-1):
    for col in range(1, len(tree_list[0])-1):
        scenic_score = find_scenic_score(row, col)
        if(scenic_score > highest_scenic_score):
            highest_scenic_score = scenic_score

print(highest_scenic_score)
