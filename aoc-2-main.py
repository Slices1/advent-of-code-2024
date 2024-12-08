def terriblyNamesFunctionToCheckSafetyForPartTwo(line):
    adjustedLine = []
    if isSafe(line):
            print("SAFE FOR PART 2")
            return True 
    for i in range(len(line)):
        # remove 'i'th term
        adjustedLine = line[:]
        print(f"line: {line}")
        print(f"adjusted line: {adjustedLine}")
        adjustedLine.pop(i)
        
        if isSafe(adjustedLine):
            print("SAFE FOR PART 2")
            return True
    return False

def isSafe(line):
    if isSafeOrder(line):
        line.sort()
        return isSafeDifference(line)
    else:
        return False

def isSafeOrder(line):
    # for i in myLinelist
    if (line == sorted(line) or line == (sorted(line))[::-1]):
        return True
    else:
        print("wrong order")
        return False
        
        

def isSafeDifference(line):
    line.sort()
    for i in range(len(line)-1):    
        if (abs(line[i] - line[i+1]) > 3 or abs(line[i] - line[i+1]) < 1):
            print("bad difference")
            return False
    return True

with open('input-2') as input:
    myLinelist = [line.rstrip('\n') for line in input]

safeCount = 0

myIntArray = []
for i in range(1000):
    # myLinelist[i].replace(" ", "")
    myLinelist[i] = (myLinelist[i].split())
    myIntArray.append(list(map(int, list(myLinelist[i]))))
    print(f"the line: {myIntArray[i]}")
    if (terriblyNamesFunctionToCheckSafetyForPartTwo(myIntArray[i])):
        print("-> safe")
        safeCount +=1;
    else:
        print("-> NOT safe")
    print(safeCount)
    # print(myLinelist)
#input = open("input-1", "r")
#print(input.readlines())
#lines = input.readlines()


