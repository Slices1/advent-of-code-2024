with open('input-10') as input:
    myLineList = [line.rstrip('\n') for line in input]
grid = []

unique9Positions = []
trailRatingSum = 0
def calculateTrailheadScore(i,j):
    global trailRatingSum
    # print(f"position x,y ={j,i} results {grid[i][j]}") # debugging
    if grid[i][j] == 9:
        if [i,j] not in unique9Positions:
            unique9Positions.append([i,j])
        trailRatingSum += 1
        return
    nextNum = int(grid[i][j]) + 1
    
    if i+1 < len(grid) and grid[i+1][j] == nextNum:
        calculateTrailheadScore(i+1,j)
    if i-1 >= 0 and grid[i-1][j] == nextNum:
        calculateTrailheadScore(i-1,j)
    if j+1 < len(grid) and grid[i][j+1] == nextNum:
        calculateTrailheadScore(i,j+1)
    if j-1 >= 0 and grid[i][j-1] == nextNum:
        calculateTrailheadScore(i,j-1)
    return

# recursive solution ?
# start on all 0s
# if neighbor tile is num + 1 call on that tile.
# if 9, and pos is unique, add pos to array
# sum them

for line in myLineList:
    grid.append(list(map(int, line)))

trailScoreSum = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            calculateTrailheadScore(i, j)
            trailScoreSum += len(unique9Positions)
            unique9Positions.clear()
            print(f"trail score sum (result1): {trailScoreSum}")
            print(f"trail rating sum (result2): {trailRatingSum}")
    #     print(grid[i][j], end='')
    # print()
