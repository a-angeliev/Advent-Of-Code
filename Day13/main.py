f = open("input.txt", "r")

lines = [eval(line) for line in f.readlines() if line != "\n"]


def compare(line1, line2):
    if isinstance(line1, int) and isinstance(line2, int):
        return line1 - line2

    if isinstance(line1, list) and isinstance(line2, list):
        l = min(len(line1), len(line2))
        for i in range(l):
            res = compare(line1[i], line2[i])
            if res != 0:
                return res
        return len(line1) - len(line2)

    if isinstance(line1, int):
        return compare([line1], line2)
    return compare(line1,[line2])


right_index = []
for line in range(0, len(lines), 2):
    if compare(lines[line],lines[line+1]) < 0:
        right_index.append(line//2+1)

index1 = sum(1 for line in lines if compare(line, [[2]]) < 0) + 1
index2 = sum(1 for line in lines if compare(line, [[6]]) < 0) + 2

print(sum(right_index))
print(index1*index2)
