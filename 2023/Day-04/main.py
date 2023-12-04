import time
start_time = time.time()

f = open("input.txt", "r")
input = f.readlines()


def find_matches(my_numbers, winning_numbers):
    numbers = []
    for num in my_numbers:
        if num in winning_numbers and num != '':
            numbers.append(num)

    return numbers


def calculate_points(matched_numbers):
    points = 0
    if len(matched_numbers) != 0:
        if len(matched_numbers) == 1:
            points = 1
        else:
            points = 1
            for i in range(len(matched_numbers)-1):
                points = points * 2

    return points


def calculate_indexes(i, indexes, matched_numbers):
    # original card
    if not i + 1 in indexes:
        indexes[i+1] = 1
    else:
        indexes[i+1] += 1

    # copy of the cards
    if len(matched_numbers) != 0:
        number_of_current_instances = indexes[i+1]
        for indx in range(len(matched_numbers)):
            index = indx+i+2
            if not index in indexes:
                indexes[index] = 1 * number_of_current_instances
            else:
                indexes[index] += 1* number_of_current_instances


def calculate_total_sum_of_cards(indexes):
    sum = 0
    for key, value in indexes.items():
        sum += int(value)

    return sum


def action():
    total_points_part1 = 0
    indexes = {}

    for i in range(len(input)):
        winning_numbers_str, my_numbers_str = input[i][10:].split(" | ")
        winning_numbers = winning_numbers_str.split(" ")
        my_numbers = my_numbers_str[:-1].split(' ')

        matched_numbers = find_matches(my_numbers, winning_numbers)

        total_points_part1 += calculate_points(matched_numbers)

        calculate_indexes(i, indexes, matched_numbers)

    total_number_of_cards_part2 = calculate_total_sum_of_cards(indexes)

    print(f"Total points for part 1: {total_points_part1}")
    print(f"Total number of cards for part 2: {total_number_of_cards_part2}")
    print(f"Time taken: {time.time() - start_time}")


action()
