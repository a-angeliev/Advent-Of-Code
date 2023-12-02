f = open("input.txt", "r")


def is_full_overlap(line):
    first_numbers = [int(num) for num in line.split(',')[0].split('-')]
    second_numbers = [int(num) for num in line.split(',')[1].split('-')]

    if first_numbers[0] <= second_numbers[0] and first_numbers[1] >= second_numbers[1]:
        return 1
    elif first_numbers[0] >= second_numbers[0] and first_numbers[1] <= second_numbers[1]:
        return 1
    return 0


def is_overlap(line):
    first_numbers = [int(num) for num in line.split(',')[0].split('-')]
    second_numbers = [int(num) for num in line.split(',')[1].split('-')]

    full_first_number_list = []
    full_second_number_list = []
    for i in range(first_numbers[0], first_numbers[1]+1):
        full_first_number_list.append(i)

    for i in range(second_numbers[0], second_numbers[1]+1):
        full_second_number_list.append(i)

    for element in full_first_number_list:
        if element in full_second_number_list:
            return 1
    return 0


input = f.readlines()
print(f"Number of overlaps is: {sum([is_full_overlap(line) for line in input])}")
print(f"Number of overlaps is: {sum([is_overlap(line) for line in input])}")