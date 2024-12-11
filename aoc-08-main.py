with open('input-8') as input:
    myLinelist = [line.rstrip('\n') for line in input]
import array as arr

def printGrid(gridInput):
    for row in gridInput:
        for character in row:
            print(character, end='')
        print()

myGrid = [] # myGrid[y][x]
myAntiNodeMap = []
for line in myLinelist:
    myGrid.append(list(line))
printGrid(myGrid)

# lowercase letter, uppercase letter, or digit

# this is going to be HARD

# assume antinodes overlapping other antinodes don't count

# 1. generate a list of all same frequency pairs storing the coords
# 2. calculate the displacements
# 3. attempt to place # at those displacements
# 4. count # and print

# 1. generate a list of all same frequency pairs storing the coords
antennas = [] # (x, y, "A")
antennaPairs = [] # [[x,y], [x,y]] # this has a pair for AB and for BA but not AA or BB
# for row in gridInput:
#     for character in row:
#         if ( ord(character) >= 48 && ord(character) ):
for i in range(len(myGrid)):
    for j in range(len(myGrid[0])):
        if not myGrid[j][i] == '.':
            # find its pairs
            antennas.append((i,j,myGrid[j][i]))
            print((i,j,myGrid[j][i]))
for antenna in antennas:
    for i in range(len(antennas)):
        if antenna[2] == antennas[i][2] and not antenna == antennas[i]:
            antennaPairs.append([[antenna[0], antenna[1]], [antennas[i][0], antennas[i][1]]])
            print([[antenna[0], antenna[1]], [antennas[i][0], antennas[i][1]]])

# 2. calculate the displacements
potentialAntinodes = [] # [A + A-B] = [2A - b]so stores A and BA direction or B and AB direction
for antennaPair in antennaPairs:
    potentialAntinodes.append([2*antennaPair[0][0] - antennaPair[1][0], 2*antennaPair[0][1] - antennaPair[1][1]])
# for i in range(len(potentialAntinodes)):
#     if potentialAntinodes[i][0] < 0 or potentialAntinodes[i][1] < 0:
#         potentialAntinodes.
potentialAntinodes = [[x,y] for x,y in potentialAntinodes if not x<0 and not y<0]
        


# 3. attempt to place # at those displacements
for potentialAntinode in potentialAntinodes:
    print(f"current potentialAntinode: {potentialAntinode}")
    try:
        myGrid[potentialAntinode[1]][potentialAntinode[0]] = '#'
    except:
        print("out of bounds")
    printGrid(myGrid)

# 4. count # and print
result1 = 0
for row in myGrid:
    for character in row:
        if character == '#':
            result1 += 1
            print(f"result1: {result1}")