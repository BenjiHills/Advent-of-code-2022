
def start_of_packet(data_string, unique_number):

    for index in range(0, len(data_string) - (unique_number-1)):
        letter_list = []
        letter_count = []
        for i in range(0, unique_number):
            letter_list.append(data_string[index + i])
            letter_count.append(letter_list.count(letter_list[i]) == 1)

        if False not in letter_count:
            return index + unique_number
            break


def get_packet_start(data_input, unique_number):
    data_string = open(data_input).read()

    return start_of_packet(data_string, unique_number)


print(f"Marker for four unique characters: {get_packet_start('puzzle_input', 4)}")
print(f"Marker for fourteen unique characters: {get_packet_start('puzzle_input', 14)}")
