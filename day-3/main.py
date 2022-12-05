priority_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def priority_cal(common_items):
    priority_sum = 0
    for item in common_items:
        priority_sum += (priority_list.index(item)+1)
    return priority_sum


def get_rucksack_list(puzzle_input):
    rucksacks = puzzle_input.split("\n")
    return rucksacks


def get_common_items(rucksacks):
    common_items = []
    for rucksack in rucksacks:
        split = int(len(rucksack)/2)
        first_pocket = rucksack[0:split]
        second_pocket = rucksack[split:]

        for item in first_pocket:
            if item in second_pocket:
                common_items.append(item)
                break
    return common_items


def get_group_badges(rucksack):
    group_badges = []
    for i in range(0, int(len(rucksack)-1), 3):
        for item in rucksack[i]:
            if item in rucksack[i+1] and item in rucksack[i+2]:
                group_badges.append(item)
                break
    return group_badges


def rucksack_prioritisation(data_input):
    rucksack_input = open(data_input).read()
    rucksacks = get_rucksack_list(rucksack_input)
    common_items = get_common_items(rucksacks)
    group_badges = get_group_badges(rucksacks)

    print(f"Number of Common Items: {priority_cal(common_items)}")
    print(f"Number of Group Badges: {priority_cal(group_badges)}")


rucksack_prioritisation("puzzle_input")
