def map_parse(data_input):
    rows = data_input.split("\n")
    number_of_row = int(rows[-1][-1])
    map_dict = {}
    for key in range(1, number_of_row + 1):
        map_dict[key] = []

    row_pointer = -2

    for row in range(1, len(rows)):
        sanitised_row = (rows[row_pointer]).replace("    ", "[?]")
        sanitised_row = sanitised_row.replace(" ", "")
        sanitised_row = sanitised_row.replace("][", "] [")
        column_pointer = 0
        for letter in sanitised_row.split(" "):
            column_pointer += 1
            if column_pointer > number_of_row:
                column_pointer = 1
            if letter != "[?]":
                map_dict[column_pointer].append(letter)
        row_pointer -= 1
    return map_dict


def instruction_parse(data_input):
    instruction_list = data_input.split("\n")
    final_instructions = []
    words = ["move", "from", 'to']
    for instruction in instruction_list:
        sanitised_instruction = []
        instruction = instruction.split(" ")
        for number in instruction:
            if number not in words:
                sanitised_instruction.append(int(number))

        final_instructions.append(sanitised_instruction)
    return final_instructions


def move_task(move, from_, to, map_dict):
    for task in range(0, move):
        number = map_dict[from_].pop(-1)
        map_dict[to].append(number)

    return map_dict


def move_reverse(move, from_, to, map_dict):
    index = -move
    for task in range(0, move):
        number = map_dict[from_].pop(index)
        map_dict[to].append(number)
        index += 1

    return map_dict


def last_item(data_input):
    map_instruction = open(data_input).read()
    map_, instruction_list = map_instruction.split("\n\n")
    map_dict = map_parse(map_)
    map_reverse = map_parse(map_)
    instructions = instruction_parse(instruction_list)
    last_items = []
    last_reversed = []

    for move, from_, to in instructions:
        move_task(move,from_, to, map_dict)
        move_reverse(move, from_, to, map_reverse)
    for value in map_dict.values():
        last_items.append(value[-1])
    for value in map_reverse.values():
        last_reversed.append(value[-1])

    print(f"Last_item in stack: {last_items}")
    print(f"Last_item in stack (reverse): {last_reversed}")


last_item("puzzle_input")