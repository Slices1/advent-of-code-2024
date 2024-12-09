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

# update left pointer (linear search rightwards from prev leftPointer pos)
for i in range(len(fileMap)):
    if fileMap[leftPointer+i] == -1:
        leftPointer = leftPointer+i
        break # should break from the for loop but no the while

while leftPointer < rightPointer:
    # print(f"left pointer: {leftPointer}, right pointer: {rightPointer}")
    # for item in fileMap:
    #     if item == -1:
    #         print(".", end='')
    #     else:
    #         print(item, end='')
    # print()

    # move item from right pointer to left
    fileMap[leftPointer] = fileMap[rightPointer]
    fileMap[rightPointer] = -1

    # upate right pointer (linear search leftwards from prev rightPointer pos)
    for i in range(len(fileMap)):
        if not fileMap[rightPointer-i] == -1:
            rightPointer = rightPointer-i
            break # should break from the for loop but no the while

    # update left pointer (linear search rightwards from prev leftPointer pos)
    for i in range(len(fileMap)):
        if fileMap[leftPointer+i] == -1:
            leftPointer = leftPointer+i
            break # should break from the for loop but no the while

# print(f"left pointer: {leftPointer}, right pointer: {rightPointer}")
# for item in fileMap:
#     if item == -1:
#         print(".", end='')
#     else:
#         print(item, end='')
# print()

checksum = 0
for i in range(leftPointer):
    checksum += fileMap[i]*i
print(f"part 1 check sum: {checksum}")


#notes and assumptions:
#diskMap has odd length