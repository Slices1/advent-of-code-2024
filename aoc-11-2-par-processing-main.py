with open('input-11') as input:
    myLinelist = [line.rstrip('\n') for line in input]
import sys
import math as maths
from concurrent.futures import ProcessPoolExecutor

def process_stone(stone):
    if stone[0] == 0:
        return [[1, stone[1]]]
    elif len(str(stone[0])) % 2 == 0:
        digits = len(str(stone[0]))
        power = 10 ** (digits // 2)
        right = stone[0] % power
        left = (stone[0] - right) // power
        
        return [[left, stone[1]], [right, stone[1]]]
    else:
        return [[stone[0] * 2024, stone[1]]]   


sys.set_int_max_str_digits(99999999)

# stones = [i][quantity]
stonesInitialiserList = list(map(int, myLinelist[0].split(" ")))
stones = [[i, 1] for i in stonesInitialiserList]
print(f"initial stones: {stones}")
print()

# must be careful to index properly when new stones are added. this is what `count` is for
for iteration in range(75):
    print(f"iteration: {iteration+1}/75")

    combined = {} # reset hash map

    # carry out rules on stones
    results = []
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(process_stone, stones))
    # print(f"results: {results}")
    flattened_results = [item for sublist in results for item in sublist]

    # print(flattened_results)

    for value, quantity in flattened_results:
        if value in combined:
            combined[value] += quantity
        else:
            combined[value] = quantity

    # convert back to a 2d list
    stones = [[value, quantity] for value, quantity in combined.items()]
    # print(stones)

    # print()

result = 0
for stone in stones:
    result += stone[1] # add stone quanitity
print(f"result: {result}")