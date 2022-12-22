class Monkey:

    def __init__(self, id, items, original_items, operator, operation, test, if_true, if_false):
        self.id = id
        self.items = items
        self.original_items = original_items
        self.operator = operator
        self.operation = operation
        self.test = test
        self.monkey_true = if_true
        self.monkey_false = if_false

    inspections = 0

    def monkey_around(self, managing, least_common):
        for i in range(0, len(self.items)):

            item = self.items.pop(0)
            self.inspections += 1
            item = eval(f"{item}  {self.operator}  {self.operation}")
            if managing:
                item = item // 3
            else:
                item = item % least_common

            if item % self.test == 0:
                monkeys[self.monkey_true].items.append(item)

            else:
                monkeys[self.monkey_false].items.append(item)




def create_monkeys(data_input):
    monkey_list = data_input.split("\n\n")
    created_monkeys = []

    for monkey in monkey_list:
        index = monkey_list.index(monkey)
        created_monkeys.append("monkey_" + str(index))
        attributes = monkey.split("\n")

        items = attributes[1].replace("Starting items: ", "").split(",")
        items = list(map(int, items))
        original_items = attributes[1].replace("Starting items: ", "").split(",")
        original_items = list(map(int, original_items))

        operation = attributes[2].split("=")[1].split(" ")
        operator = operation[-2]
        if operation[-1] == "old":
            operation = "item"
        else:
            operation = int(operation[-1])

        test = int(attributes[3].split(" ")[-1])
        if_true = int(attributes[4].split(" ")[-1])
        if_false = int(attributes[5].split(" ")[-1])

        created_monkeys[index] = Monkey(created_monkeys[index],
                                        items, original_items,
                                        operator, operation,
                                        test, if_true, if_false)
    return created_monkeys


monkey_input = open("test_input").read()
monkeys = create_monkeys(monkey_input)


def monkey_business(rounds, managing):
    least_common = 1
    for monkey in monkeys:
        least_common *= monkey.test

    for r in range(0, rounds):
        for monkey in monkeys:
            monkey.monkey_around(managing, least_common)

    inspection_list = sorted([monkey.inspections for monkey in monkeys])

    for monkey in monkeys:
        monkey.items = monkey.original_items
        monkey.inspections = 0

    return inspection_list[-1] * inspection_list[-2]


print(monkey_business(20, True))
print(monkey_business(10000, False))
