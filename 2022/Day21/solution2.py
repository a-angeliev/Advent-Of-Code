# !!!! This is modified foreign solution !!!
import time

start = time.time()
f = open('input.txt', "r")

monkeys = {}
marked = set()
for line in f.readlines():
    name, right_site = line.split(": ")
    right_site = right_site.removesuffix("\n").split(" ")
    if len(right_site) == 1:
        monkeys[name] = [int(right_site[0])]
    else:
        monkeys[name] = [right_site[0], right_site[1], right_site[2]]

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

# res = arg1 [op] x
reverse_operations_arg1 = {
    "+": lambda x, res: res - x,
    "-": lambda x, res: res + x,
    "*": lambda x, res: res / x,
    "/": lambda x, res: res * x,
}

# res = x [op] arg2
reverse_operations_arg2 = {
    "+": lambda x, res: res - x,
    "-": lambda x, res: x - res,
    "*": lambda x, res: res / x,
    "/": lambda x, res: x / res,
}


def mark_path(monkey):
    if monkey == "humn":
        marked.add(monkey)
        return True

    if len(monkeys[monkey]) == 1:
        return False

    arg1, arg2 = monkeys[monkey][0], monkeys[monkey][2]
    if mark_path(arg1) or mark_path(arg2):
        marked.add(monkey)
        return True


def get_value(monkey):
    if len(monkeys[monkey]) == 3:
        arg1, op, arg2 = monkeys[monkey]
        return operations[op](get_value(arg1), get_value(arg2))
    else:
        return int(monkeys[monkey][0])


def expect_value(monkey, expect):
    if monkey == "humn":
        return expect

    arg1, op, arg2 = monkeys[monkey]

    if arg1 in marked:
        arg2_value = get_value(arg2)
        new_expect = reverse_operations_arg1[op](arg2_value, expect)
        return expect_value(arg1, new_expect)
    else:
        arg1_value = get_value(arg1)
        new_expect = reverse_operations_arg2[op](arg1_value, expect)
        return expect_value(arg2, new_expect)


mark_path("root")
left, right = monkeys["root"][0], monkeys["root"][2]
if left in marked:
    expected = get_value(right)
    answer = expect_value(left, expected)
else:
    expected = get_value(left)
    answer = expect_value(right, expected)

print(f"Part 2: {int(answer)}")

print(time.time() - start)
