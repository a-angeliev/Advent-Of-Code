import time
start_time = time.time()

f = open("input.txt", "r")
input = f.readlines()

total_sum = 0
line_number = ""

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for line in input:
    new_line = ''
    first = False
    for i in range(len(line)):
        new_line += line[i]
        for key, value in digits.items():
            new_line = new_line.replace(key, value)
        for digit in new_line:
            if digit.isnumeric():
                line_number += digit
                first = True
                break
        if first:
            break

    new_line = ''
    second = False
    for i in range(len(line)-1,-1,-1):
        new_line = line[i] + new_line
        for key, value in digits.items():
            new_line = new_line.replace(key, value)
        for digit in new_line:
            if digit.isnumeric():
                line_number += digit
                second = True
                break
        if second:
            break

    total_sum += int(line_number)
    line_number = ""

print(total_sum)
print(time.time()-start_time)