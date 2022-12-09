with open("inputs/day-9.txt", "r") as ifile:
    instructions = [f.strip() for f in ifile.readlines()]

moves = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
positions, known_positions = {f: [0, 0] for f in range(10)}, set()
for command in instructions:
    com, param = command.split(" ")
    vector = moves[com]
    for rep in range(int(param)):
        positions[0][0] += vector[0]
        positions[0][1] += vector[1]
        for knot in range(1, 10):
            adj_fn = int if (dst := abs((x_diff := positions[knot-1][0] - positions[knot][0])) + abs(y_diff := positions[knot-1][1] -
                             positions[knot][1])) < 3 else lambda x: round(x + ((md := (min((x_diff, y_diff), key=abs)))/abs(md if md != 0 else 1))*0.1)
            positions[knot][0] += adj_fn((positions[knot-1]
                                         [0] - positions[knot][0]) / 2)
            positions[knot][1] += adj_fn((positions[knot-1]
                                         [1] - positions[knot][1]) / 2)
        known_positions.add(tuple(positions[9]))

print("Known_tail_positions: {}".format(len(known_positions)))
