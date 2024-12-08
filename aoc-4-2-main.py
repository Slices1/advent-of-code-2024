with open('input-4') as input:
    myLinelist = [line.rstrip('\n') for line in input]

print(myLinelist)


# diagonal
# or written backwards
# X shaped MAS

result2 = 0

# diagonal down-right / up-left
for i in range(len(myLinelist)-2):
    for j in range(len(myLinelist[0])-2):
        # print(f"i,j = {i},{j}")
        mySplice = ''.join([myLinelist[i][j], myLinelist[i+1][j+1], myLinelist[i+2][j+2]])
        #print(f"diagonal down right splice: {mySplice}")
        if (mySplice == 'MAS' or mySplice == 'SAM'):
            otherSplice = ''.join([myLinelist[i+2][j], myLinelist[i+1][j+1], myLinelist[i][j+2]])
          
            if (otherSplice == 'MAS' or otherSplice == 'SAM'):
                result2 += 1;
                print(f"result2: {result2}")
                





# diagonal down-right / up-left
