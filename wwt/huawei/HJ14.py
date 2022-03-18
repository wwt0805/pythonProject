"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/18 下午1:41
@Site   : 
@File   : HJ14.py
@SoftWare: PyCharm
"""


def hj_14():
    data_list = []
    num = input()
    for i in range(int(num)):
        data = input()
        data_list.append(data)
    data_list.sort()

    for _ in data_list:
        print(_)


if __name__ == '__main__':
    hj_14()
