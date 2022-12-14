def map_parse(map_data):
    all_trees = []
    map_list = map_data.split("\n")
    for row in map_list:
        new_row = []
        for number in row:
            new_row.append(int(number))
        all_trees.append(new_row)

    return all_trees


def get_hidden_trees(all_trees):
    total_trees = 0
    hidden_trees = 0
    max_score = 0

    for tree_row in all_trees:
        index = all_trees.index(tree_row)
        total_trees += len(tree_row)
        scenic_score = row_scenic(all_trees, tree_row, index)

        if max_score < scenic_score:
            max_score = scenic_score

        if tree_row != all_trees[0] and tree_row != all_trees[-1]:
            hidden_trees += row_check(all_trees, tree_row, index)

    return total_trees, hidden_trees, max_score


def row_check(all_trees, tree_row, row_index):
    hidden_tree = 0
    for i in range(1, len(tree_row) - 1):
        check_passed_left = []
        check_passed_right = []
        for j in range(0, i):
            check_passed_left.append(tree_row[i] <= tree_row[j])
        for j in range(i + 1, len(tree_row)):
            check_passed_right.append(tree_row[i] <= tree_row[j])
        if True in check_passed_left and True in check_passed_right:
            hidden_tree += colum_check(all_trees, tree_row[i], row_index, i)

    return hidden_tree


def colum_check(all_trees, tree, row, colum):
    check_passed_top = []
    check_passed_bottom = []

    for i in range(0, row):
        check_passed_top.append(tree <= all_trees[i][colum])

    for i in range(row + 1, len(all_trees)):
        check_passed_bottom.append(tree <= all_trees[i][colum])

    if True in check_passed_top and True in check_passed_bottom:
        return 1
    else:
        return 0


def row_scenic(all_trees, tree_row, row_index):
    max_score = 0
    for i in range(0, len(tree_row)):
        left_score = 0
        right_score = 0

        for j in reversed(range(0, i)):
            left_score += 1

            if tree_row[i] <= tree_row[j]:
                break

        for j in range(i + 1, len(tree_row)):
            right_score += 1

            if tree_row[i] <= tree_row[j]:
                break

        top_score, bottom_score = colum_scenic(all_trees, tree_row[i], row_index, i)
        tree_score = left_score * right_score * top_score * bottom_score

        if max_score < tree_score:
            max_score = tree_score

    return max_score


def colum_scenic(all_trees, tree, row, colum):
    top_score = 0
    bottom_score = 0

    for i in reversed(range(0, row)):
        top_score += 1

        if tree <= all_trees[i][colum]:
            break

    for i in range(row + 1, len(all_trees)):
        bottom_score += 1

        if tree <= all_trees[i][colum]:
            break

    return top_score, bottom_score


def get_visible_trees(data_input):
    map_data = open(data_input).read()
    tree_list = map_parse(map_data)

    total_trees, hidden_trees, scenic_score = get_hidden_trees(tree_list)

    visible_trees = total_trees - hidden_trees

    print(f"Number of Visible Trees: {visible_trees}")
    print(f"Max Scenic Score: {scenic_score}")


get_visible_trees("puzzle_input")
