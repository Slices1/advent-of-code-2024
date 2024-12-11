with open('input-11') as input:
    myLinelist = [line.rstrip('\n') for line in input]
import sys
import math as maths

sys.set_int_max_str_digits(99999999)

# stones = [i][quantity]

# stonesInitialiserList = list(map(int, myLinelist[0].split(" ")))
# stones = [[i, 1] for i in stonesInitialiserList]
stones = [[1,1],]

# print(f"initial stones: {stones}")
# print()

# must be careful to index properly when new stones are added. this is what `count` is for
for iteration in range(1000000):
    # print(f"iteration: {iteration+1}/100,003")

    combined = {} # reset hash map

    # carry out rules on stones
    for stone in stones:

        if stone[0] == 0:
            if 1 in combined:
                combined[1] += stone[1] # add quantity
            else:
                combined[1] = stone[1]
            
        elif len(str(stone[0])) % 2 == 0:
            digits = maths.floor(maths.log10(stone[0])) + 1
            power = 10 ** (digits // 2)
            
            myQuantity = stone[1]
            # print(f"my quantity: {myQuantity}")

            # value = int(myStone[:length//2])
            value = stone[0] % power
            if value in combined:
                combined[value] += myQuantity
            else:
                combined[value] = myQuantity
                
            # value = int(myStone[length//2:])
            value = (stone[0] - value) // power
            if value in combined:
                combined[value] += myQuantity
            else:
                combined[value] = myQuantity

        else:
            value = stone[0] * 2024
            if value in combined:
                combined[value] += stone[1]
            else:
                combined[value] = stone[1]

    # convert back to a 2d list
    stones = [[value, quantity] for value, quantity in combined.items()]
    # print(stones)


result = 0
for stone in stones:
    result += stone[1] # add stone quanitity
print(f"result: {result}")