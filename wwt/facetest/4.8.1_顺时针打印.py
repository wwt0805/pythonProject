'''
假定有一个二维数组，要求将数组中的元素以顺时针螺旋方式打印出来，例如：
1 2 3
4 5 6
7 8 9
顺时针打印出来即为123698745
'''
import numpy as np


def rotation(num: int):
    '''
    思路：
    1.根据输入参数构建矩阵；
    2.设置上下左右四个指针；
    3.根据四个指针的运动防方向构建循环输出；
    4.当上下指针，左右指针分别指向相同时，停止程序
    :param num:
    :return: 返回顺时针输出矩阵结果。
    '''
    matrix = np.array(np.arange(1, num ** 2 + 1)).reshape(num, num)
    print(matrix)
    top = 0
    right = num - 1
    bottom = num - 1
    left = 0

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            print(matrix[top][i], end=',')
        for i in range(top + 1, bottom + 1):
            print(matrix[i][right], end=',')
        for i in range(bottom - 1, left - 1, -1):
            print(matrix[bottom][i], end=',')
        for i in range(bottom - 1, top, -1):
            print(matrix[i][left], end=',')

        top += 1
        right -= 1
        bottom -= 1
        left += 1


if __name__ == '__main__':
    rotation(4)
