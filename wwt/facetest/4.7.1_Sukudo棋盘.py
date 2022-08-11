'''
Sukudo棋盘是一种逻辑游戏，他由9X9的网格组成，玩法是要求每一行，每一列、每个3X3的子网格都有1-9九个数字填充，并且每行每列每个子网格填充的
数字都不重复，给定一个9X9的二维数组，请给出满足条件的填充算法
'''


class Sukudo:
    def __init__(self):
        self.sukudoBoard = [[0] * 9 for i in range(9)]


if __name__ == '__main__':
    s = Sukudo()
    print(s.sukudoBoard)
