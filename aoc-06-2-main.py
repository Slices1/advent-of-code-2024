with open('input-6') as input:
    myLinelist = [line.rstrip('\n') for line in input]
# import time

def loopsForever(x, y, i, j, myGridCopy):
    myGridCopy[i][j] = '#'
    myPositionSet = set([(x, y, '^')]) # hash set
    # print(myPositionSet)

    # use myPositionSet.update((i, j, directions[directionIndex]))
    nextX = x
    nextY = y

    directions = ['^', '>', 'v', '<']
    directionIndex = 0 # facing up

    # print("does it endlessly loop? new obstacle placement is below:")
    while True:
        # for row in range(len(myGridCopy)):
        #     for column in range(len(myGridCopy[0])):
        #         print(myGridCopy[row][column], end='')
        #     print()
        # print()
        # print()
        # print()
        # print()
        # time.sleep(1)
        # for move in myPositionSet:
        #     print(move)
        
        
        # we have position
        # we have direction
        # we need to find next position
        match directionIndex:
            case 0:
                nextY += -1
            case 1:
                nextX += 1
            case 2:
                nextY += 1
            case 3:
                nextX += -1

        # check if next move is out of bounds
        if nextY < 0 or nextY >= len(myGridCopy) or nextX < 0 or nextX >= len(myGridCopy[0]):
            myGridCopy[i][j] = '.' # revert to unaltered state
            # print("final state:")
            # print(myPositionSet)
            return False

        # check if blocked
        if (myGridCopy[nextY][nextX] == '#'):
            #turn
            directionIndex = (directionIndex + 1) % 4
            nextY = y
            nextX = x
        else:
            #move
            # myGridCopy[y][x] = directions[directionIndex]
            # myGridCopy[nextY][nextX] = directions[directionIndex]
            myPositionSet.add((x, y, directions[directionIndex]))
            y=nextY
            x=nextX
            
        # check if looping
        if (x, y, directions[directionIndex]) in myPositionSet: 
            myGridCopy[i][j] = '.' # revert to unaltered state
            # print("sucess!!!")
            # print("final state:")
            # print(myPositionSet)
            return True
            



myGrid = []
myGridCopy = []
for line in myLinelist:
    myGrid.append(list(line))
    myGridCopy.append(list(line))


# part 2
# only check tiles that the guard would previously go through
# it will loop if it appears back on a previous position IN THE SAME DIRECTION
# assume loops where it crosses its previous path multiple times overwriting the direction dont exist (or resolve themselves)


# startPos = [4,6]
startPos = [96,43]

print(len(myGrid))
print("before")
for row in myGrid:
    for character in row:
        print(character, end='')
    print()


x = startPos[0]
y = startPos[1]

nextX = x
nextY = y

directions = ['^', '>', 'v', '<']
directionIndex = 0
# directionIndex = (directionIndex + 1) % 4

while True:
    try:
            # we have position
            # we have direction
            # we need to find next position
            match directionIndex:
                case 0:
                    nextY += -1
                case 1:
                    nextX += 1
                case 2:
                    nextY += 1
                case 3:
                    nextX += -1
            # check if blocked
            if (myGrid[nextY][nextX] == '#'):
                #turn
                directionIndex = (directionIndex + 1) % 4
                nextY = y
                nextX = x
            else:
                # part 2: here you need to check if they'll be the same
                myGrid[y][x] = directions[directionIndex]
                myGrid[nextY][nextX] = directions[directionIndex]
                y=nextY
                x=nextX

        # print("during")
        # for row in myGrid:
        #     for character in row:
        #         print(character, end='')
        #     print()

    except:
        print("Exception occured. Likely out of bounds")
        break

print("after")
for row in myGrid:
    for character in row:
        print(character, end='')
    print()

result1 = 0
visitedPositions = [] # stores [y,x] coords atm annoyingly
for i in range(len(myGrid)):
    for j in range(len(myGrid[i])):
        if myGrid[i][j] in directions:
            result1 += 1
            visitedPositions.append([i, j])
visitedPositions.remove(startPos[::-1]) #y,x format
# visitedPositions.remove([6,4]) #y,x format
print(f"visited positions: {visitedPositions}")
print(f"visited positions length: {len(visitedPositions)}")
for i in range(len(myGrid)):
    for j in range(len(myGrid[0])):
        if [i, j] in visitedPositions:
            print("X", end='')
        else:
            print(".", end='')
    print()

result2 = 0
for position in visitedPositions:
    # print(f"attempting position: {position}")
    if loopsForever(startPos[0], startPos[1], position[0], position[1], myGridCopy):
        result2 += 1
        # print(f"position {position} was succesful")
        # print(f"result2: {result2}")

# if loopsForever(startPos[0], startPos[1], 6, 3, myGridCopy):
#         result2 += 1

print(f"result1: {result1}")
print(f"result2: {result2}")

# print("blank copy:")
# for row in myGridCopy:
#     for character in row:
#         print(character, end='')
#     print()
#y,x valid coords for example:
#6,3
#7,6
#7,7
#8,1
#8,3
#9,7


# if doesnt work for rectangle shapes, tweak line 46