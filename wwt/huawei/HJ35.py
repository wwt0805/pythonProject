"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/23 下午5:35
@Site   : 
@File   : HJ35.py
@SoftWare: PyCharm
"""


def hj_35():
    num = int(input())
    for index in range(1, num):
        for column in range(index, num, column+1):
            print(column, end=" ")


if __name__ == '__main__':
    hj_35()
