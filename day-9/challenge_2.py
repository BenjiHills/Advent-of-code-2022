def move_right(coordinate):
    coordinate[0] += 1


def move_left(coordinate):
    coordinate[0] -= 1


def move_down(coordinate):
    coordinate[1] -= 1


def move_up(coordinate):
    coordinate[1] += 1


class Rope:
    knot_coord = []
    positions_visited = [[0, 0]]

    def get_knot_coordinates(self, num_knots):
        for knot in range(0, num_knots):
            self.knot_coord.append([0, 0])

    def start_move(self, direction):
        if direction == "U":
            move_up(self.knot_coord[0])

        if direction == "D":
            move_down(self.knot_coord[0])

        if direction == "L":
            move_left(self.knot_coord[0])

        if direction == "R":
            move_right(self.knot_coord[0])

    def does_knot_move(self, knot_2):
        knot_1 = knot_2 - 1

        if self.knot_coord[knot_1][1] == self.knot_coord[knot_2][1]:
            if abs(self.knot_coord[knot_1][0] - self.knot_coord[knot_2][0]) in [0, 1]:
                return False
        if self.knot_coord[knot_1][0] == self.knot_coord[knot_2][0]:
            if abs(self.knot_coord[knot_1][1] - self.knot_coord[knot_2][1]) in [0, 1]:
                return False

        return True

    def knot_move(self, direction, knot_2):
        knot_1 = knot_2 - 1

        front_knot = self.knot_coord[knot_1]
        back_knot = self.knot_coord[knot_2]

        dif_x = front_knot[0] - back_knot[0]
        dif_y = front_knot[1] - back_knot[1]
        if abs(dif_x) <= 1 and abs(dif_y) <= 1:
            return
        if abs(dif_x) < abs(dif_y):
            back_knot[0] = front_knot[0]
            back_knot[1] = front_knot[1] - dif_y // 2

        elif abs(dif_y) < abs(dif_x):
            back_knot[1] = front_knot[1]
            back_knot[0] = front_knot[0] - dif_x // 2

        else:
            back_knot[0] = front_knot[0] - dif_x // 2
            back_knot[1] = front_knot[1] - dif_y // 2

    def move(self, direction, turns, knots):
        for turn in range(0, int(turns)):

            for knot in range(0, knots):
                if knot == 0:
                    self.start_move(direction)

                else:
                    if self.does_knot_move(knot):
                        self.knot_move(direction, knot)

                        if self.knot_coord[-1] not in self.positions_visited:
                            self.positions_visited.append(self.knot_coord[-1][:])

    def unique_tail_positions(self):
        print(self.positions_visited)
        return len(self.positions_visited)


def get_unique_tail_positions(data_input, knots):
    instructions = open(data_input).read()
    instr_list = instructions.split("\n")
    rope = Rope()
    rope.get_knot_coordinates(knots)

    for instr in instr_list:
        instr = instr.split(" ")
        rope.move(instr[0], instr[1], knots)

    print(rope.unique_tail_positions())


get_unique_tail_positions("puzzle_input", 10)
