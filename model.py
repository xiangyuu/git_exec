"""
數據模型
"""

class DirectionModel:
    """
    方向數據模型
    枚舉 常量
    """
    UP=0
    DOWN=1
    LEFT=2
    RIGHT=3

class Location:
    """
    位置
    """
    def __init__(self,r,c):
        self.r_index=r
        self.c_index=c
