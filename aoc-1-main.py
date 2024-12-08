with open('input-1') as input:
#input = open("input-1", "r")
#print(input.readlines())
#lines = input.readlines()
    myLinelist = [line.rstrip('\n') for line in input]
# print(myLinelist)
leftArr = []
rightArr =[]

rightIntColumn = []
leftIntColumn = []


result = 0
for i in range(1000):
    leftArr.append("temp")
    rightArr.append("temp")
    leftArr[i], rightArr[i] = myLinelist[i].split("   ", 1)
    # rightIntColumn.append(1);
    # leftIntColumn.append(1);
#     #rightIntColumn[i] = sorted(list(map(int, list(rightArr[i]))))
#     #leftIntColumn[i] = sorted(list(map(int, list(leftArr[i]))))

#     for j in range(1):
#         result += abs(rightIntColumn[i][j] - leftIntColumn[i][j])
#         print()
#         print(f"{rightIntColumn[i][j]} - {leftIntColumn[i][j]} = {abs(rightIntColumn[i][j] - leftIntColumn[i][j])}")
#         print(f"result: {result}")

# print(leftArr)
# print(rightArr)
# print(leftIntColumn)
# print(rightIntColumn)

leftIntColumn = sorted(list(map(int, leftArr)))
rightIntColumn = sorted(list(map(int, rightArr)))
for i in range (1000):
    result += abs(leftIntColumn[i] - rightIntColumn[i])
    print(f"result: {result}")


secondResult = 0
appearances =0
for lhsNumber in leftIntColumn:
    appearances = 0
    for value in rightIntColumn:
        if (value == lhsNumber):
            appearances += 1;
    secondResult += lhsNumber*appearances
    print(f"second part result: {secondResult}")

input.close()