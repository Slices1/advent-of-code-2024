with open('input-11') as input:
    myLinelist = [line.rstrip('\n') for line in input]
import math 

stones = list(map(int, myLinelist[0].split(" ")))
print(f"after iteration: 0\n {stones}")

# must be careful to index properly when new stones are added. this is what `count` is for
for iteration in range(25):
    print(f"iteration: {iteration}/75")
    count = 0
    for i in range(len(stones)):
        if stones[count] == 0:
            stones[count] = 1
        elif len(str(stones[count])) % 2 == 0:
            # print()
            # print()
            # print(f"{stones[count]} is even")
            # print("even num of digits")
            # calc length
            # insert after [i] the number [0:length//2]
            # insert after [i+1] the number [length//2:length]
            # remove [i]
            # increment i???
            length = len(str(stones[count]))
            # print(f"length: {length}")
            # print(f"count is {count}")
            # print(f"attempting to insert start with bounds: {0, length//2}")
            # print(f"attempting to insert: {str(stones[count])[0:length//2]}")
            stones.insert(count+1, int(str(stones[count])[:length//2]))
            # print(f"after 1st insert: {stones}")
            # print(f"attempting to insert start with bounds: {length//2, length}")
            # print(f"attempting to insert: {str(stones[count])[length//2:]}")
            stones.insert(count+2, int(str(stones[count])[length//2:]))
            # print(f"after 2nd insert: {stones}")
            del stones[count]
            # print(f"after deletion: {stones}")

            count += 1
        else:
            stones[count] *= 2024
        count += 1
    # print(f"\nafter iteration: {iteration+1}\n {stones}")


result1 = len(stones)
print(f"result1: {result1}")


# input:
#7725 185 2 132869 0 1840437 62 26310
# count of factors of 2 input:
#0 0 1 0 0 0 0 1