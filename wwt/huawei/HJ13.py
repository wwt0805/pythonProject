"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/18 下午1:34
@Site   : 
@File   : HJ13.py
@SoftWare: PyCharm
"""


def hj_13():
    data = input().split(" ")
    data.reverse()
    for _ in data:
        print(_, end=" ")


if __name__ == '__main__':
    hj_13()
