f = open("input.txt", "r")


def symbol_score(symbol):
    if symbol.islower():
        return ord(symbol) - 96
    return ord(symbol) - 38


def find_same_in_half(line):
    for e in line[0: len(line)//2]:
        if line[len(line)//2: len(line)-1].__contains__(e):
            return symbol_score(e)


def find_same_for_group(line1, line2, line3):
    for e in line1:
        if line2.__contains__(e) and line3.__contains__(e):
            return symbol_score(e)


input = f.readlines()

print(f"Total Score: {sum([find_same_in_half(line) for line in input])}")
print(f"Sum of the item types: {sum([find_same_for_group(input[i], input[i+1], input[i+2]) for i in range(0, len(input), 3)])}")