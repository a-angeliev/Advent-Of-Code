from functools import reduce
f = open("input.txt", "r")

monkeys = []


class Monkey:
    def __init__(self, items, op, test, if_true, if_false):
        self.items = items
        self.op = op
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.inspect_count = 0

    def calculate_worry(self, item_worry):
        if self.op[0] == "old":
            a = f"{item_worry}"
        else:
            a = self.op[0]

        operatior = self.op[1]

        if self.op[2] == "old":
            b = f"{item_worry}"
        else:
            b = self.op[2]

        return eval(a+operatior+b)


starting_items = []
operation = []
test = int
if_true = int
if_false = int

for line in f.readlines():
    if line.startswith("  Starting items:"):
        starting_items = [int(x.removesuffix(",")) for x in line.removesuffix('\n').split(" ")[4:]]
    elif line.startswith("  Operation:"):
        operation = [x for x in line.removesuffix('\n').split(" ")[5:]]
    elif line.startswith("  Test:"):
        test = int(line.removesuffix('\n').split(" ")[5:][0])
    elif line.startswith("    If true:"):
        if_true = int(line.removesuffix('\n').split(" ")[9])
    elif line.startswith("    If false:"):
        if_false = int(line.removesuffix('\n').split(" ")[9])

    if line.strip() == "":
        monkeys.append(Monkey(starting_items,operation,test, if_true,if_false))

        starting_items = []
        operation = []
        test = int
        if_true = int
        if_false = int

monkeys.append(Monkey(starting_items,operation,test, if_true,if_false))

no_changing_test_number = 1
for monkey in monkeys:
    no_changing_test_number *= monkey.test

for _ in range(10000):

    for i in range(len(monkeys)):
        monkey = monkeys[i]

        for _ in range(len(monkey.items)):
            worry = monkey.calculate_worry(monkey.items[0])
            monkey.inspect_count += 1
            get_bored_worry = worry % no_changing_test_number
            poped_item = monkey.items.pop(0)
            if get_bored_worry % monkey.test == 0:
                monkeys[monkey.if_true].items.append(get_bored_worry)
            else:
                monkeys[monkey.if_false].items.append(get_bored_worry)


sorted_inspections = sorted([monkey.inspect_count for monkey in monkeys], reverse=True)[0:2]
inspect_result = reduce(lambda x, y: x*y, sorted_inspections)
print(f"Part2 :{inspect_result}")

