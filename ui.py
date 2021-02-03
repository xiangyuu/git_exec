from bll import *
from  model import *
import os
"""
    2048控制台界面
"""

class GameConsoleView:
    def __init__(self):
        self.__controller=GameCoreController()
    def main(self):
        self.__start()
        self.__update()

    def __start(self):
        # 產生兩個數
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        # 繪製界面
        self.__draw_map()
    def __draw_map(self):
        # 清空控制台
        os.system("clear")
        for line in self.__controller.map:
            for item in line:
                print(item,end=" ")
            print(" ")

    def __update(self):
        # 循環
        while True:
            # 判斷玩家的輸入-->移動地圖
            self.move_map_for_input()
            # 產生新數字
            self.__controller.generate_new_number()
            # 繪製界面
            self.__draw_map()
            # 遊戲結束判斷-->提示
            if self.__controller.is_game_over():
                print("遊戲結束")
                break


    def move_map_for_input(self):
        dir=input("請輸入方向(wsad)")
        dict_dir={
            "w": DirectionModel.UP,
            "s": DirectionModel.DOWN,
            "a": DirectionModel.LEFT,
            "d": DirectionModel.RIGHT
        }
        if dir in dict_dir:
            self.__controller.move(dict_dir[dir])

# ------------------------
if __name__=="__main__":
    view=GameConsoleView()
    view.main()







