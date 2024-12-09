with open('input-9') as input:
    diskMap = list(list(input)[0])
diskMap.remove('\n')
print(diskMap)

# 1 2 3 4 5
# ID,file: 0,0  1,111, 2,22222

fileMap = []

for i in range((len(diskMap)-1)//2):  
    # print(f"working on diskmap numbers: {diskMap[2*i]} and {diskMap[2*i+1]}")
    for j in range(int(diskMap[2*i])):
        fileMap.append(i)
    for j in range(int(diskMap[2*i+1])):
        fileMap.append(-1) # '.'
# dont forget last item:
for j in range(int(diskMap[-1])):
        fileMap.append((len(diskMap))//2)

# for item in fileMap:
#     if item == -1:
#         print(".", end='')
#     else:
#         print(item, end='')
# print()













rightPointer = len(fileMap)-1
# print(fileMap[lastItemPointer])
leftPointer = 0

freePointerLeft = 0
freePointerRight = 0
freeSpaces = []

filePointerLeft = 99999
filePointerRight = len(fileMap) - 1

while filePointerLeft > 0:
    # print()
    # print()
    # print()
    # print()

    # for item in fileMap:
    #     if item == -1:
    #         print(".", end='')
    #     else:
    #         print(item, end='')
    # print()

    #update file pointers
    # while free spaces left:
        #update free space pointers
        # if theres space, move

    #note: you have to make sure free space is to the left of the file

    #update file pointers
    for i in range(len(fileMap)):
        if not fileMap[filePointerRight-i] == -1:
            filePointerRight = filePointerRight -i
            break 
    for i in range(len(fileMap)):
        if not fileMap[filePointerRight-i] == fileMap[filePointerRight]:
            filePointerLeft = filePointerRight-i+1
            break 

    # print(f"filePointerLeft: {filePointerLeft}, filePointerRight: {filePointerRight}")

    #update free space pointers
    freePointerLeft=0
    freePointerRight=0
    freeSpaces.clear()
    try:
        for j in range(len(fileMap) // 2): # check for all free spaces 
            for i in range(len(fileMap)):
                if fileMap[freePointerLeft+i] == -1:
                    freePointerLeft = freePointerLeft+i
                    break 
            for i in range(len(fileMap)):
                if not fileMap[freePointerLeft+i] == -1:
                    freePointerRight = freePointerLeft+i-1
                    break
            # print(f"freePointerLeft: {freePointerLeft}, freePointerRight: {freePointerRight}")
            freeSpaces.append([freePointerLeft, freePointerRight])
            # print(f"free space added: {[freePointerLeft, freePointerRight]}")
            freePointerLeft = freePointerRight+1
    except:
        pass
        # print(f"free spaces: {freeSpaces}")

    lengthOfFile = filePointerRight - filePointerLeft+1
    for freeSpace in freeSpaces:
        lengthOfFreeSpace = freeSpace[1]-freeSpace[0]+1
        if lengthOfFile <= lengthOfFreeSpace and freeSpace[0] < filePointerLeft:
            #move
            for i in range(lengthOfFile):
                fileMap[freeSpace[0]+i] = fileMap[filePointerLeft+i]
                fileMap[filePointerLeft+i] = -1
            break
    filePointerRight = filePointerLeft - 1

    






print(f"freePointerLeft: {freePointerLeft}, freePointerRight: {freePointerRight}, filePointerLeft: {filePointerLeft}, filePointerRight: {filePointerRight}")
for item in fileMap:
    if item == -1:
        print(".", end='')
    else:
        print(item, end='')
print()












checksum = 0
for i in range(len(fileMap)):
    if not fileMap[i] == -1: 
        checksum += fileMap[i]*i
print(f"part 1 check sum: {checksum}")


#notes and assumptions:
#diskMap has odd length