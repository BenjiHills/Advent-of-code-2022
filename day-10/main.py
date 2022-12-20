class Screen(object):

    def __init__(self, data_input, cycle_list):
        self.data_input = data_input
        self.cycle_list = cycle_list
        self.program_list = self.get_program_list()

    total_strength = 0

    crt_cycle = 0
    signal_strength = 1
    row_1 = ""
    row_2 = ""
    row_3 = ""
    row_4 = ""
    row_5 = ""
    row_6 = ""

    def get_program_list(self):
        program = open(self.data_input).read()
        program_list = program.split("\n")

        return program_list

    def signal_strength_cal(self, total_cycles):
        signal_strength = 1
        cycles = 0

        while cycles < total_cycles:
            for program in self.program_list:

                if "noop" in program:
                    cycles += 1
                if "addx" in program:
                    cycles += 2
                    if cycles >= total_cycles:
                        break
                    strength = int(program.replace("addx ", ""))
                    signal_strength += strength

            break

        return signal_strength * total_cycles

    def total_strength_cal(self):
        for cycle in self.cycle_list:
            signal = self.signal_strength_cal(cycle)
            self.total_strength += signal
        return self.total_strength

    def get_image(self):
        for program in self.program_list:
            if "noop" in program:
                self.add_to_image()

            if "addx" in program:
                self.add_to_image()
                self.add_to_image()
                strength = int(program.replace("addx ", ""))
                self.signal_strength += strength

            if self.crt_cycle == 240:
                self.print_image()

    sprite_position = [signal_strength, signal_strength + 1, signal_strength + 2]

    def print_image(self):
        self.crt_cycle = 0
        screen = [self.row_1,
                  self.row_2,
                  self.row_3,
                  self.row_4,
                  self.row_5,
                  self.row_6
                  ]
        for row in screen:
            print(row)
        print(" ")

    def add_to_image(self):
        sprite_position = [self.signal_strength, self.signal_strength + 1, self.signal_strength + 2]

        self.crt_cycle += 1

        self.row_1 += self.light_pixel(1, 41)
        self.row_2 += self.light_pixel(41, 81)
        self.row_3 += self.light_pixel(81, 121)
        self.row_4 += self.light_pixel(121, 161)
        self.row_5 += self.light_pixel(161, 201)
        self.row_6 += self.light_pixel(201, 241)

        if self.crt_cycle >= 240:
            self.print_image()

    def light_pixel(self, lower_range, upper_range):
        sprite_position = [self.signal_strength, self.signal_strength + 1, self.signal_strength + 2]

        if self.crt_cycle in range(lower_range, upper_range):
            crt_position = self.crt_cycle - (lower_range - 1)

            if crt_position in sprite_position:
                return "#"
            else:
                return "."
        return ""


all_cycles = [20, 60, 100, 140, 180, 220]

radio = Screen("puzzle_input", all_cycles)

print(radio.total_strength_cal())

radio.get_image()
