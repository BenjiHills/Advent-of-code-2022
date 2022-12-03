def list_create(data_input):
    rounds = data_input.split("\n")
    round_list = []
    for match in rounds:
        match = match.split(" ")
        round_list.append(match)
    return round_list


# part 1
wins = [['A', 'Y'], ['B', 'Z'], ['C', 'X']]  # A = rock     X = rock
draws = [['A', 'X'], ['B', 'Y'], ['C', 'Z']]  # B = paper    Y = paper
scores = {'X': 1, 'Y': 2, 'Z': 3}  # C = scissors Z = scissors

# part 2
wining_hand = {'A': ['A', 'Y'], 'B': ['B', 'Z'], 'C': ['C', 'X']}  # X = lose
drawing_hand = {'A': ['A', 'X'], 'B': ['B', 'Y'], 'C': ['C', 'Z']}  # Y = draw
losing_hand = {'A': ['A', 'Z'], 'B': ['B', 'X'], 'C': ['C', 'Y']}  # Z = win
outcomes = {'X': losing_hand, 'Y': drawing_hand, 'Z': wining_hand}


def match_cal(round_list):  # solution for part 1
    points = 0

    for match in round_list:
        points += scores[match[1]]
        if match in wins:
            points += 6
        elif match in draws:
            points += 3
    return points


def decrypt_and_cal(round_list):  # solution for part 2
    new_list = []

    for match in round_list:
        outcome = outcomes[match[1]]
        new_list.append(outcome[match[0]])

    return match_cal(new_list)


def points_calculator(data_input):
    rounds = open(data_input).read()
    rounds_list = list_create(rounds)

    part_1_score = match_cal(rounds_list)
    part_2_score = decrypt_and_cal(rounds_list)

    print(f'score 1: {part_1_score}')
    print(f'score 2: {part_2_score}')


points_calculator("problem_input")


