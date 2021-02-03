"""
遊戲邏輯控制器,負責處理遊戲核心算法
"""
from model import DirectionModel
from model import Location
import random
class GameCoreController:

    def __init__(self):
        self.__list_merge=None
        self.__map = [[0, 0, 0,0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
        self.__list_empty_location=[]

    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        """
        將0移至末尾
        """
        for i in range(-1, -len(self.__list_merge) - 1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merge(self):
        """
        將相同數字合併
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def __movie_left(self):
        """
        向左移動
        """
        for line in self.__map:
            self.__list_merge = line
            self.__merge()


    def __movie_right(self):
        """
        向右移動
        """
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            line[::-1] = self.__list_merge

    def __movie_up(self):
        """
        向上移動
        """
        self.__square_matrix_transpose()
        self.__movie_left()
        self.__square_matrix_transpose()

    def __movie_down(self):
        """
        向下移動
        """
        self.__square_matrix_transpose()
        self.__movie_right()
        self.__square_matrix_transpose()

    def __square_matrix_transpose(self):
        """
        方陣轉置
        :param map: 將列表行列對調
        """
        for i in range(len(self.__map)):
            for c in range(i, len(self.__map)):
                if self.__map[i][c] != self.__map[c][i]:
                    self.__map[i][c], self.__map[c][i] = self.__map[c][i], self.__map[i][c]

    def move(self,dir):
        """
        移動
        :param dir:方向 DirectionModel類型
        """
        if dir ==DirectionModel.UP:
            self.__movie_up()
        elif dir ==DirectionModel.DOWN:
            self.__movie_down()
        elif dir ==DirectionModel.LEFT:
            self.__movie_left()
        elif dir ==DirectionModel.RIGHT:
            self.__movie_right()


    def generate_new_number(self):
        """
            生成新數字
        """

        self.__get_empty_location()
        if len(self.__list_empty_location)==0:
            return
        loc=random.choice(self.__list_empty_location)
        # if random.randint(1,10)==1:
        #     self.map[loc.r_index][loc.c_index]=4
        # else:
        #     self.map[loc.r_index][loc.c_index]=2
        self.map[loc.r_index][loc.c_index]=4 if random.randint(1,10)==1 else 2
        # 因為在該位置生成了新數字,所以該位置就不是空位置了
        self.__list_empty_location.remove(loc)
    def __get_empty_location(self):
        self.__list_empty_location.clear()
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                if self.map[r][c] == 0:
                    self.__list_empty_location.append(Location(r,c))

    def is_game_over(self):
        """
        遊戲是否結束
        :return: False表示沒有結束
        """
        if len(self.__list_empty_location)>0:
            return False

        # for r in range(len(self.__map)):
        #     for c in range(len(self.__map)-1):
        #         if self.__map[r][c]==self.__map[r][c+1]:
        #             return False
        #
        # for c in range(len(self.__map)):
        #     for r in range(len(self.__map)-1):
        #         if self.__map[r][c]==self.__map[r+1][c]:
        #             return False
        for r in range(len(self.__map)):
            for c in range(len(self.__map)-1):
                if self.__map[r][c]==self.__map[r][c+1] or self.__map[c][r]==self.__map[c+1][r]:
                    return False
        return True


# ---------測試代碼------------------
if __name__=="__main__":
    controller=GameCoreController()
    # controller.movie_down()
    # print(controller.map)
    # controller.move(DirectionModel.LEFT)
    # print(controller.map)

    controller.generate_new_number()
    controller.generate_new_number()
    controller.generate_new_number()
    controller.generate_new_number()

    controller.is_game_over()
    print(controller.map)