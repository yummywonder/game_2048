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


"""
    ２０４８游戏
    规则：
        游戏运行，在４＊４的方格中，出现两个随机的数字．
        产生随机数的策略：10%的概率是４，90%的概率是2.
        用户移动方格（wsad）,方格内的数字按照相应规则进行合并．
        如果地图有变化(数字移动／数字合并)，再产生１个随机数．
        游戏结束：数字不能合并，也没有空白位置．
    架构：
            逻辑处理模块     　　　　　　　　　Controller
            界面视图模块(控制台／pygame/.....)View
            数据模型模块..
            程序入口模块
    步骤：
    　　（一）逻辑处理模块 
             创建游戏核心类GameCoreController
             (1)将核心算法粘贴进来16:32
             (2)将所有参数，改为成员变量．16:50
             (3)产生新数字
             　　　-- 计算所有空白位置(为０的位置).
                   -- 随机选择一个位置
                   -- 根据概率产生数字，存入列表的相应位置．
         （二）界面视图模块
         　　　创建游戏核心类对象
         　　　调用核心类对象的生成数字方法
            　　while True:
                  呈现界面
                  获取用户输入，调用核心类对象的移动方法．　
                  产生随机数
        　(三)如果地图有变化(数字移动／数字合并)，再产生１个随机数．
        　(四)游戏结束：数字不能合并，也没有空白位置．

"""









