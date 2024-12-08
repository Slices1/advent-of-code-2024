with open('input-8') as input:
    myLinelist = [line.rstrip('\n') for line in input]
import array as arr

myGrid = [] # myGrid[y][x]
myAntiNodeMap = []
for line in myLinelist:
    myGrid.append(list(line))

# 1. generate a list of all same frequency pairs storing the coords
antennas = [] # (x, y, "A")
antennaPairs = [] # [[x,y], [x,y]]
for i in range(len(myGrid)):
    for j in range(len(myGrid[0])):
        if not myGrid[j][i] == '.':
            # find its pairs
            antennas.append((i,j,myGrid[j][i]))
for antenna in antennas:
    for i in range(len(antennas)):
        if antenna[2] == antennas[i][2] and not antenna == antennas[i]:
            antennaPairs.append([[antenna[0], antenna[1]], [antennas[i][0], antennas[i][1]]])

# 2. calculate the displacements
potentialAntinodes = [] # [A + A-B] = [2A - b]so stores A and BA direction or B and AB direction
for antennaPair in antennaPairs:
    displacementX = antennaPair[0][0] - antennaPair[1][0]
    displacementY = antennaPair[0][1] - antennaPair[1][1]
    for i in range(35):
        potentialAntinodes.append([antennaPair[0][0] + i*displacementX, antennaPair[0][1] + i*displacementY])

potentialAntinodes = [[x,y] for x,y in potentialAntinodes if not x<0 and not y<0]

# 3. attempt to place # at those displacements
for potentialAntinode in potentialAntinodes:
    try:
        myGrid[potentialAntinode[1]][potentialAntinode[0]] = '#'
    except:
        print("it wants me to put something after this except...")

# 4. count # and print
result2 = 0
for row in myGrid:
    for character in row:
        if character == '#':
            result2 += 1
print(f"result2: {result2}")