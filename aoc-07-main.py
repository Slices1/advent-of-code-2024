with open('input-7') as input:
    myLinelist = [line.rstrip('\n') for line in input]

def couldPossiblyBeTrue(targetNum, values):
    #possibilities = 2 ^ (amount of values - 1)
    #recursive?
    # try  1+2+3
    # then 1*2+3
    # then 1+2*3
    # then 1*2*3

    # each operator is either + or *, its kind of binary
    # we need every combination of binary up to amount of values
    # we can increment a binary number to do this

    # it is evaluated from left to right, so we need to keep a running total I think..

    binaryCounter = 0
    runningTotal = 0

    while binaryCounter < pow(2, (len(values) - 1)): #    the possibilities
        binaryBits = [int(i) for i in "{0:016b}".format(binaryCounter)][::-1]
        # print(binaryBits)
               
        if binaryBits[0]: # +
            runningTotal = values[0] + values[1]
        else: # *
            runningTotal = values[0] * values[1]


        for i in range(len(values)-2): # each gap minus the one above
            if binaryBits[i+1]: # +
                runningTotal = runningTotal + values[i+2]
            else: # *
                runningTotal = runningTotal * values[i+2]

        binaryCounter += 1
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
    print(testValues[i])
    print(numbers[i])


result1 = 0
for i in range(len(testValues)):
    if couldPossiblyBeTrue(testValues[i], numbers[i]):
        result1 += testValues[i]
        print(f"result1: {result1}")
# if couldPossiblyBeTrue(5, [1,2,3]):
#     print("success")