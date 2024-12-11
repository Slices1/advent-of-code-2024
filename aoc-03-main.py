import re

with open('input-3') as input:
    myLinelist = [line.rstrip('\n') for line in input]

flattened_list = ''.join(myLinelist)

print("before part 2 processing")
print(flattened_list)
part2Input = re.sub("don't\(\).*?do\(\)", "", flattened_list)
print("after part 2 processing")
print(part2Input)


# mulMatches = re.findall("mul\([0-9]{1,3},.{1,3}\)", flattened_list)
mulMatches = re.findall("mul\([0-9]{1,3},.{1,3}\)", part2Input)

print(mulMatches)

result1 = 0

for item in mulMatches:
    print()
    print(item)
    parts = re.split(",", item)
    print(parts)
    lhs = int(re.findall("[0-9]{1,3}", parts[0])[0])
    rhs = int(re.findall("[0-9]{1,3}", parts[1])[0])
    print(lhs)
    print(rhs)
    result1 += lhs * rhs
    print(result1)