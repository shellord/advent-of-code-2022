FILE_PATH = "inputs/day-9.txt"
data = open(FILE_PATH, 'r')


record = [[0, 0]]


def findCoveredPositions(posHead, posTail, direction):
    rowOfTail = posTail[0]
    colOfTail = posTail[1]
    rowOfHead = posHead[0]
    colOfHead = posHead[1]

    # if in same row
    if(rowOfTail == rowOfHead):
        if(direction == 'R'):
            for i in range(colOfTail+1, colOfHead):
                record.append([rowOfTail, i])
                print("move to ", record[-1])
        elif(direction == 'L'):
            for i in range(posTail[1], posHead[1], -1):
                record.append([rowOfTail, i])
                print("move to ", record[-1])

    # if in same col
    elif(colOfHead == colOfTail):
        if(direction == 'U'):
            for i in range(rowOfTail+1, rowOfHead):
                record.append([i, colOfTail])
                print("move to ", record[-1])
        elif(direction == 'D'):
            for i in range(rowOfTail, rowOfHead, -1):
                record.append([i, colOfTail])
                print("move to ", record[-1])

    # if in diagonal
    else:
        if((abs(colOfHead-colOfTail) == 1) and (abs(rowOfHead-rowOfTail) == 1)):
            return
        if(colOfHead > colOfTail):
            colOfTail += 1
        else:
            colOfTail -= 1
        if(rowOfHead > rowOfTail):
            rowOfTail += 1
        else:
            rowOfTail -= 1

        record.append([rowOfTail, colOfTail])
        print("move to ", record[-1])
        findCoveredPositions(posHead, record[-1], direction)


posHead = [0, 0]
posTail = [0, 0]

for i in data:
    direction = i.split(' ')[0]
    distance = int(i.split(' ')[1])

    if(direction == 'R'):
        posHead[1] += distance
    elif(direction == 'L'):
        posHead[1] -= distance
    elif(direction == 'U'):
        posHead[0] += distance
    elif(direction == 'D'):
        posHead[0] -= distance

    findCoveredPositions(posHead, record[-1], direction)


uniqueCells = []

for i in record:
    if i not in uniqueCells:
        uniqueCells.append(i)

print(len(uniqueCells))
