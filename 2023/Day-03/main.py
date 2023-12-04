import time
start_time = time.time()

f = open("input.txt", "r")
input = f.readlines()

row_last_index = len(input[139])-1
col_last_index = len(input)-1

number = ""
indexes = set()
numbers = []


for row in range(len(input)):

    for i in range(len(input[row])):
        if input[row][i].isnumeric():
            indexes.add((row-1,i))
            indexes.add((row+1,i))
            indexes.add((row,i+1))
            indexes.add((row,i-1))
            indexes.add((row-1,i-1))
            indexes.add((row-1,i+1))
            indexes.add((row+1,i-1))
            indexes.add((row+1,i+1))

            number += input[row][i]
        else:
            if number != '':
                numbers.append([number, indexes])
                indexes = set()
            number = ""

total_sum = 0

for i in range(len(numbers)):
    number, ind = numbers[i]

    for row, i in ind:
        if 0<=row <=col_last_index and 0<= i <= row_last_index:
            if not input[row][i].isnumeric() and input[row][i] != ".":
                total_sum += int(number)
                break
print(total_sum)
print(time.time() - start_time)

num = []
sum_part2 = 0
for row in range(len(input)):
    for i in range(len(input[row])):
        if input[row][i] == "*":
            for pair in numbers:
                n, coor = pair

                if (row, i) in coor:
                    num.append(n)

            if len(num) == 2 :
                sum_part2 += int(num[0]) * int(num[1])
            num = []

print(sum_part2)
print(time.time() - start_time)