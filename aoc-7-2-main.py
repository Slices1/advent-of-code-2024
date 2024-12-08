with open('input-7') as input:
    myLinelist = [line.rstrip('\n') for line in input]

def couldPossiblyBeTrue(targetNum, values):
    #possibilities = 3 ^ (amount of values - 1)
    #recursive?
    # try  1+2+3
    # then 1*2+3
    # then 1+2*3
    # then 1*2*3

    ternaryCounter = 0
    runningTotal = 0
    ternaryBits = [0 for i in range(11)]

    while ternaryCounter < pow(3, (len(values) - 1)): #    the possibilities
        #calculate a ternary bit array
        tempTernaryCounter = ternaryCounter
        for i in range(11): # 11 is the most we'll need
            ternaryBits[i] = tempTernaryCounter % 3
            tempTernaryCounter = tempTernaryCounter // 3
        # print(ternaryBits)
               
        if ternaryBits[0] == 0: # +
            runningTotal = values[0] + values[1]
        elif ternaryBits[0] == 1: # *
            runningTotal = values[0] * values[1]
        else: # ||
            runningTotal = int(str(values[0]) + str(values[1]))
        # else:
        #     print("this shouldnt be happening. the ternary bits went above value of 2")


        for i in range(len(values)-2): # each gap minus the one above
            if ternaryBits[i+1] == 0: # +
                runningTotal = runningTotal + values[i+2]
            elif ternaryBits[i+1] == 1: # *
                runningTotal = runningTotal * values[i+2]
            else: # ||
                runningTotal = int(str(runningTotal) + str(values[i+2]))
            # else:
            #     print("this shouldnt be happening. the ternary bits went above value of 2")

        # increment
        ternaryCounter += 1

        if runningTotal == targetNum:
            return True
    return False

testValues = []
numbers = []
for i in range(len(myLinelist)):
    testValues.append('')
    numbers.append('')
    testValues[i], numbers[i] = myLinelist[i].split(": ", 1)
    numbers[i] = list(map(int, numbers[i].split(" ")))
    testValues[i] = int(testValues[i])
    # print(testValues[i])
    # print(numbers[i])


result2 = 0
for i in range(len(testValues)):
    if couldPossiblyBeTrue(testValues[i], numbers[i]):
        result2 += testValues[i]
        print(f"result2: {result2}")
# if couldPossiblyBeTrue(5, [1,2,3]):
#     print("success")