"""

"""
import random

class GameCoreController:
    """

    """
    def __init__(self):
        self.map = [
            [0]*4,
            [0]*4,
            [0]*4,
            [0]*4
        ]
        self.list_merge = []

    def zero_to_end(self):
        for i in range(len(self.list_merge) - 1, -1, -1):
            if self.list_merge[i] == 0:
                del self.list_merge[i]
                self.list_merge.append(0)

    def merge(self):
        self.zero_to_end()
        for i in range(len(self.list_merge) - 1):
            if self.list_merge[i] == self.list_merge[i + 1]:
                self.list_merge[i] += self.list_merge[i + 1]
                self.list_merge[i + 1] = 0
        self.zero_to_end()


    def move_left(self):
        for r in range(len(self.map)):
            self.list_merge[:] = self.map[r]
            self.merge()
            self.map[r][:] = self.list_merge

    def move_right(self):
        for r in range(len(self.map)):
            self.list_merge[:] = self.map[r][::-1]
            self.merge()
            self.map[r][::-1] = self.list_merge

    def move_up(self):
        for c in range(4):
            self.list_merge.clear()
            for r in range(4):
                self.list_merge.append(self.map[r][c])
            self.merge()
            for r in range(4):
                self.map[r][c] = self.list_merge[r]

    def move_down(self):
        for c in range(4):
            self.list_merge.clear()
            for r in range(3, -1, -1):
                self.list_merge.append(self.map[r][c])
            self.merge()
            for r in range(3, -1, -1):
                self.map[r][c] = self.list_merge[3 - r]

    def get_empty(self):
        list = []
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                if self.map[r][c] == 0:
                    list.append((r, c))
        return list

    def gen_new_number(self):
        if len(self.get_empty()) == 0:
            return
        else:
            lucky_position = random.choice(self.get_empty())
            if random.randint(1,10) < 10:
                lucky_number = 2
            else:
                lucky_number = 4
            self.map[lucky_position[0]][lucky_position[1]] = lucky_number

    def get_max(self):
        max0 = max(self.map[0])
        for r in range(1,len(self.map)):
            if max0 < max(self.map[r]):
                max0 = max(self.map[r])
        return max0






def print_map(map):
    print("--------------------------")
    for r in range(len(map)):
        for c in range(len(map[r])):
            print(map[r][c],end=' ')
        print()



if __name__ == "__main__":
    core = GameCoreController()
    print_map(core.map)
    core.move_down()
    print_map(core.map)
    core.gen_new_number()
    print_map(core.map)
    core.gen_new_number()
    print_map(core.map)
    core.gen_new_number()
    print_map(core.map)











