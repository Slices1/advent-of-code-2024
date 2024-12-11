with open('input-4') as input:
    myLinelist = [line.rstrip('\n') for line in input]

print(myLinelist)
result1 = 0

# horizontal
for i in range(len(myLinelist)):
    print(f"current line: {myLinelist[i]}")
    for j in range(len(myLinelist[i])-3):
        print(f"curent forward splice: {myLinelist[i][j:j+4]}")
        if (myLinelist[i][j:j+4] == 'XMAS'):            # forwards
            result1 += 1;
            print(f"result: {result1}")
        print(f"curent backward splice: {myLinelist[i][j:j+4][::-1]}")
        if (myLinelist[i][j:j+4] == 'SAMX'):            # backwards
            result1 += 1;
            print(f"result: {result1}")

        
# vertical
for j in range(len(myLinelist[0])):
    for i in range(len(myLinelist)-3):
        mySplice = ''.join([myLinelist[i][j], myLinelist[i+1][j], myLinelist[i+2][j], myLinelist[i+3][j]])
        print(mySplice)
        if (mySplice == 'XMAS'):
            result1 += 1;
            print(result1)
        if (mySplice == 'SAMX'):
            result1 += 1;
            print(result1)

# diagonal down-right / up-left
for i in range(len(myLinelist)-3):
    for j in range(len(myLinelist[0])-3):
        mySplice = ''.join([myLinelist[i][j], myLinelist[i+1][j+1], myLinelist[i+2][j+2], myLinelist[i+3][j+3]])
        print(f"diagonal down right splice: {mySplice}")
        if (mySplice == 'XMAS'):
            result1 += 1;
            print(result1)
        if (mySplice == 'SAMX'):
            result1 += 1;
            print(result1)
# diagonal up-right / down-left
for i in range(len(myLinelist)-3):
    for j in range(len(myLinelist[0])-3):
        col = len(myLinelist[0]) - j -1
        mySplice = ''.join([myLinelist[i][col], myLinelist[i+1][col-1], myLinelist[i+2][col-2], myLinelist[i+3][col-3]])
        print(f"diagonal down left splice: {mySplice}")
        if (mySplice == 'XMAS'):
            result1 += 1;
            print(result1)
        if (mySplice == 'SAMX'):
            result1 += 1;
            print(result1)