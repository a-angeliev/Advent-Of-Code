import time

start = time.time()
f = open("input.txt", "r")
list_of_numbers = [int(x) for x in f.readlines()]


def iterate_numbers(numbers, iterations=1, multiply=1):
    numbers = [int(x) * multiply for x in numbers]

    numbers_indexes = [i for i in range(len(numbers))]
    NUM = len(numbers_indexes) - 1

    for i in range((NUM + 1) * iterations):

        i = i % (NUM + 1) if iterations != 1 else i

        path = numbers[i]
        old_index = numbers_indexes.index(i)

        if path > 0:
            new_index = old_index + path % NUM
            new_index = new_index % NUM if new_index > NUM else new_index
        if path < 0:
            new_index = (old_index - (abs(path) % NUM))
            if new_index <= 0:
                new_index = - (abs(new_index) % NUM)
                new_index = NUM + new_index

        new_index = old_index if path == 0 else new_index

        numbers_indexes.pop(old_index)
        numbers_indexes.insert(new_index, i)

    new_numbers = [numbers[x] for x in numbers_indexes]

    index_zero = new_numbers.index(0)
    result = sum([new_numbers[x] for x in [index_zero + 1000, index_zero + 2000, index_zero + 3000]])

    return result


MULTIPLY = 811589153
ITERATIONS = 10
print(f"Part 1: {iterate_numbers(list_of_numbers)}")
print(f"Part 2: {iterate_numbers(list_of_numbers, ITERATIONS, MULTIPLY)}")
print(time.time() - start)
