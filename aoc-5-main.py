with open('input-5-1') as input:
    myRuleLinelist = [line.rstrip('\n') for line in input]
with open('input-5-2') as input:
    myUpdateLinelist = [line.rstrip('\n') for line in input]
# import random # was for bogosort
from functools import cmp_to_key


def updateBreaksRules(update, rules):
    # get indice of first nums of rule
    # get indice of second nums of rule
    # all second nums must be after first numbs -> max(first indices) < min(second indices)
    for rule in rules:
        firstIndices = [i for i, j in enumerate(update) if j == rule[0]]
        secondIndices = [i for i, j in enumerate(update) if j == rule[1]]

        if (firstIndices and secondIndices):
            if max(firstIndices) > min(secondIndices):
                return True
    return False

# def orderCorrectly(update, rules):
#     # recursively do a breadth first search
#     # put each value in rules order
#     updateCopy = update[:]
#     output = []
#     for rule in rules:
#         lhsPageMatches = [j for i, j in enumerate(updateCopy) if j == rule[0]] # every first page
#         output += lhsPageMatches
#         updateCopy = [i for i in updateCopy if i != rule[0]]
#         rhsPageMatches = [j for i, j in enumerate(updateCopy) if j == rule[1]] # every first page
#         output += rhsPageMatches
#         updateCopy = [i for i in updateCopy if i != rule[1]]
#     return output

def compare(item1, item2):
    if [item1, item2] in rules:4130
        return -1
    if [item2, item1] in rules:
        return 1
    return 0



print(myRuleLinelist)
print(myUpdateLinelist)

rules = []
for i in range(len(myRuleLinelist)):
    rules.append(list(map(int, myRuleLinelist[i].split("|", 1))))
print(rules)

updates = []
for i in range(len(myUpdateLinelist)):
    updates.append(list(map(int, myUpdateLinelist[i].split(","))))
print(updates)

#part 2
#there are no duplicate numbers so we can create a mapping from number to indice:
# numberToIndice = []
# for rule in rules:
#     numberToIndice.append(-1)
#     numberToIndice.append(-1)

# numberToIndice = [i for i in numberToIndice if i != -1] # filter out the placeholders




result1 = 0
result2 = 0
for update in updates:
    print(update)
    if updateBreaksRules(update, rules):
        print("invalid")
        # fix thingy, then sum middles
    #     update = orderCorrectly(update, rules)
        print(f"before sort: {update}")
        update.sort(key=cmp_to_key(compare))
        print(f"after sort: {update}")
    #     print(f"CORRECTED ORDER: {update}")    # did it work??
        
        if updateBreaksRules(update, rules):
            print("my custom sort didnt work :(")
        else:
            print(f"Now is Valid. adding middle: {update[len(update)//2]}")
            result2 += update[len(update)//2] # middle
            print(f"Result2: {result2}")

    else:
        print(f"Valid. adding middle: {update[len(update)//2]}")
        result1 += update[len(update)//2] # middle
        print(f"Result1: {result1}")

print(f"resul1 again: {result1}")
print(f"resul2 again: {result2}")