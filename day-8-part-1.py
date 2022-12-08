FILE_PATH = "inputs/day-8.txt"
data = open(FILE_PATH, 'r')


tree_list = []

for i in data:
    tree_list.append(i.strip())


no_of_tree_in_edges = len(tree_list[0]) * 4 - 4


def is_visible_from_outside(row, col):
    is_visible_from_top = True
    is_visible_from_bottom = True
    is_visible_from_left = True
    is_visible_from_right = True

    # check is visible from top
    for i in range(0, row):
        if(tree_list[i][col] >= tree_list[row][col]):
            is_visible_from_top = False
            break

    # check is visible from bottom
    for i in range(row+1, len(tree_list[0])):
        if(tree_list[i][col] >= tree_list[row][col]):
            is_visible_from_bottom = False
            break

    # check is visible from left
    for i in range(0, col):
        if(tree_list[row][i] >= tree_list[row][col]):
            is_visible_from_left = False
            break

    # check if visible from right
    for i in range(col+1, len(tree_list[0])):
        if(tree_list[row][i] >= tree_list[row][col]):
            is_visible_from_right = False
            break

    if((not is_visible_from_bottom) and (not is_visible_from_top) and (not is_visible_from_left) and (not is_visible_from_right)):
        return False

    return True


count_of_trees_visible = 0


for row in range(1, len(tree_list[0])-1):
    for col in range(1, len(tree_list[0])-1):
        if(is_visible_from_outside(row, col)):
            count_of_trees_visible += 1


total_visible_tress = count_of_trees_visible + no_of_tree_in_edges
print(total_visible_tress)
