with open('input-6') as input:
    myLinelist = [line.rstrip('\n') for line in input]

# for line in myLinelist:
#     print(line)




myGrid = []
for line in myLinelist:
    myGrid.append(list(line))

myGrid[0][0] = 'a'
myGrid[1][0] = 'b'
myGrid[0][1] = 'c'

print("before")
for row in myGrid:
    for character in row:
        print(character, end='')
    print()

currentPos = [4, 6]
# currentPos = [96, 43]
# currentPos = [currentPos[0]-1, currentPos[1]]
while True:
    try:
        if (myGrid[currentPos[1]][currentPos[0]] == '^'):  # up
            if (myGrid[currentPos[1]-1][currentPos[0]] == '#'): # blocked
                myGrid[currentPos[1]][currentPos[0]] = '>'
            else:
                myGrid[currentPos[1]][currentPos[0]] = 'X'
                myGrid[currentPos[1]-1][currentPos[0]] = '^'
                currentPos = [currentPos[0], currentPos[1]-1]
        elif (myGrid[currentPos[1]][currentPos[0]] == '>'):  # right
            if (myGrid[currentPos[1]][currentPos[0]+1] == '#'): # blocked
                myGrid[currentPos[1]][currentPos[0]] = 'v'
            else:
                myGrid[currentPos[1]][currentPos[0]] = 'X'
                myGrid[currentPos[1]][currentPos[0]+1] = '>'
                currentPos = [currentPos[0]+1, currentPos[1]]
        elif (myGrid[currentPos[1]][currentPos[0]] == 'v'):  # down
            if (myGrid[currentPos[1]+1][currentPos[0]] == '#'): # blocked
                myGrid[currentPos[1]][currentPos[0]] = '<' # I assumed this is the character it wants
            else:
                myGrid[currentPos[1]][currentPos[0]] = 'X'
                myGrid[currentPos[1]+1][currentPos[0]] = 'v'
                currentPos = [currentPos[0], currentPos[1]+1]
        elif (myGrid[currentPos[1]][currentPos[0]] == '<'):  # left
            if (myGrid[currentPos[1]][currentPos[0]-1] == '#'): # blocked
                myGrid[currentPos[1]][currentPos[0]] = '^'
            else:
                myGrid[currentPos[1]][currentPos[0]] = 'X'
                myGrid[currentPos[1]][currentPos[0]-1] = '<'
                currentPos = [currentPos[0]-1, currentPos[1]]
        else:
            print("this shouldnt be happening. no if cases were triggered")
        
        print(f"current direction: {myGrid[currentPos[1]][currentPos[0]]}")
        # print("during")
        # for row in myGrid:
        #     for character in row:
        #         print(character, end='')
        #     print()

    except:
        print("Exception occured. Likely out of bounds")
        break;

print("after")
for row in myGrid:
    for character in row:
        print(character, end='')
    print()

result1 = 1 # for final position that hasnt been set to 'X'

for row in myGrid:
    for character in row:
        if character == 'X':
            result1 += 1
print(f"result1: {result1}")