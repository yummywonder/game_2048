from bll import *

class GameView:
    def __init__(self):
        self.core = GameCoreController()


    def print_view(self):
        for r in range(len(self.core.map)):
            for c in range(len(self.core.map[r])):
                print(self.core.map[r][c], end=' ')
            print()

    def start(self):
        self.core.gen_new_number()
        self.core.gen_new_number()
        self.print_view()

    def get_user_action(self):
        action = input("please select a direction from wasd:")
        if action == 'w':
            self.core.move_up()
        if action == 'a':
            self.core.move_left()
        if action == 's':
            self.core.move_down()
        if action == 'd':
            self.core.move_right()

    def update(self):
        while True:
            if self.core.get_max() == 2048:
                print("you win,congratulations!")
                break
            map_old = self.core.map
            self.get_user_action()
            self.core.gen_new_number()
            map_new = self.core.map
            if map_new != map_old:
                self.print_view()
            elif map_new == map_old and len(self.core.get_empty()) != 0:
                self.print_view()
                continue
            else:
                print('sad,you lost!')


