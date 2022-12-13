import random


def file_space_dict(data_input):
    dir_list = data_input.split("$ cd")
    dir_dict = {}
    all_files = []

    for dirs in dir_list:
        dirs = dirs.lstrip()
        dirs = dirs.split("\n\n")
        for direct in dirs:
            files = direct.split("\n")
            all_files.append(files)

    outer_total = 0
    for files in all_files:
        for file in files:
            file_size = "".join(filter(str.isdigit, file))
            if file_size != "":
                outer_total += int(file_size)

        if files[0] != "/":
            directory = files[0] + str(random.randint(1111, 9999))

            total_size = dir_count(files, all_files)

        if total_size > 0:
            dir_dict[directory] = total_size

    dir_dict["/"] = outer_total

    return dir_dict


def dir_count(files, all_files):
    dir_size = 0
    for file in files:

        if "dir" in file:
            indirect = file.replace("dir", "").lstrip()
            for i in range(all_files.index(files) + 1, len(all_files)):
                if indirect == all_files[i][0]:
                    dir_size += dir_count(all_files[i], all_files)
                    break

        file_size = "".join(filter(str.isdigit, file))
        if file_size != "":
            dir_size += int(file_size)
    return dir_size


def less_than_hundred_thousand(dir_dict):
    total = 0

    for val in dir_dict.values():
        if val <= 100000:
            total += val
    return total


def space_save(dir_dict):
    free_space = 70000000 - dir_dict["/"]
    space_needed = 30000000 - free_space
    suitable_directories = []

    for val in dir_dict.values():
        if val >= space_needed:
            suitable_directories.append(val)

    suitable_directories.sort(reverse=True)
    smallest_file = suitable_directories.pop()

    return smallest_file


def file_size_cal(data_input):
    directories = open(data_input).read()
    test_dict = file_space_dict(directories)

    total_under_100000 = less_than_hundred_thousand(test_dict)
    smallest_delete = space_save(test_dict)

    print(f"Total Size For Files Under Hundred Thousand: {total_under_100000}")
    print(f"Smallest Deletable File Size: {smallest_delete}")


file_size_cal("puzzle_input")
