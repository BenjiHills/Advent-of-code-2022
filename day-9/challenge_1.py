def move_right(coordinate):
    coordinate[0] += 1


def move_left(coordinate):
    coordinate[0] -= 1


def move_down(coordinate):
    coordinate[1] -= 1


def move_up(coordinate):
    coordinate[1] += 1


class Rope:
    h_coord = [0, 0]
    t_coord = [0, 0]
    t_positions = [[0, 0]]

    def head_move(self, direction):
        if direction == "U":
            move_up(self.h_coord)

        if direction == "D":
            move_down(self.h_coord)

        if direction == "L":
            move_left(self.h_coord)

        if direction == "R":
            move_right(self.h_coord)

    def does_tail_move(self):
        if self.h_coord[1] == self.t_coord[1]:
            if abs(self.h_coord[0] - self.t_coord[0]) in [0, 1]:
                return False
        if self.h_coord[0] == self.t_coord[0]:
            if abs(self.h_coord[1] - self.t_coord[1]) in [0, 1]:
                return False

        return True

    def tail_move(self, direction):
        if self.h_coord[0] != self.t_coord[0] and self.h_coord[1] != self.t_coord[1]:

            if (self.h_coord[1] - self.t_coord[1]) == 2:
                move_up(self.t_coord)
                self.t_coord[0] = self.h_coord[0]

            if self.h_coord[1] - self.t_coord[1] == -2:
                move_down(self.t_coord)
                self.t_coord[0] = self.h_coord[0]

            if self.h_coord[0] - self.t_coord[0] == 2:
                move_right(self.t_coord)
                self.t_coord[1] = self.h_coord[1]

            if self.h_coord[0] - self.t_coord[0] == -2:
                move_left(self.t_coord)
                self.t_coord[1] = self.h_coord[1]
        else:
            if direction == "U":
                move_up(self.t_coord)

            if direction == "D":
                move_down(self.t_coord)

            if direction == "L":
                move_left(self.t_coord)

            if direction == "R":
                move_right(self.t_coord)

    def move(self, direction, turns):
        for turn in range(0, int(turns)):
            self.head_move(direction)

            if self.does_tail_move():
                self.tail_move(direction)

                if self.t_coord not in self.t_positions:
                    self.t_positions.append(self.t_coord[:])

    def unique_tail_positions(self):
        return len(self.t_positions)


def get_unique_tail_positions(data_input):
    instructions = open(data_input).read()
    instr_list = instructions.split("\n")
    rope = Rope()

    for instr in instr_list:
        instr = instr.split(" ")
        rope.move(instr[0], instr[1])

    print(rope.unique_tail_positions())

get_unique_tail_positions("puzzle_input")
