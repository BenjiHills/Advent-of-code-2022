def containment_counter(data_input):
    pairs_list = data_input.split("\n")
    totally_contained = 0
    any_contained = 0

    for pair in pairs_list:
        both_coordinates = pair.split(",")

        coordinate_1 = both_coordinates[0].split("-")
        coordinate_2 = both_coordinates[1].split("-")

        long_range = range(int(coordinate_1[0]), int(coordinate_1[1]) + 1)
        short_range = range(int(coordinate_2[0]), int(coordinate_2[1]) + 1)

        if len(short_range) > len(long_range):

            hold_range = long_range
            long_range = short_range
            short_range = hold_range

        contained_num = 0

        for num in short_range:
            if num in long_range:
                contained_num += 1
        if contained_num == len(short_range):
            totally_contained += 1
        if contained_num >= 1:
            any_contained += 1

    return f"Areas Completely Contained: {totally_contained}", f"Areas With Any Overlap: {any_contained}"


def number_of_areas_contained(data_input):
    areas_input = open(data_input).read()
    totally_contained, any_contained = containment_counter(areas_input)

    print(totally_contained)
    print(any_contained)


number_of_areas_contained("puzzle_input")
