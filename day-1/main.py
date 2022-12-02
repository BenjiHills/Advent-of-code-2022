def elf_calories(calorie_input):
    elves = calorie_input.split("\n\n")
    calorie_sum = []

    for elf in elves:
        calorie = 0
        elf = elf.split("\n")
        for snack in elf:
            calorie += int(snack)
        calorie_sum.append(calorie)
    return sorted(calorie_sum)


def challenge_1(calorie_sum):
    return calorie_sum[-1]


def challenge_2(calorie_sum):
    return calorie_sum[-1] + calorie_sum[-2] + calorie_sum[-3]


def lembas(data_input):
    test_problem = open(data_input).read()

    calorie_list = elf_calories(test_problem)
    answer_1 = challenge_1(calorie_list)
    answer_2 = challenge_2(calorie_list)

    print(answer_1)
    print(answer_2)


lembas('problem_input')
