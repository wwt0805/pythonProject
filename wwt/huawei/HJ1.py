"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/18 上午10:23
@Site   : 
@File   : HJ1.py
@SoftWare: PyCharm
"""


def hj_1():
    word = input()
    lastword = word.split(" ")[-1]
    return len(lastword)


if __name__ == '__main__':
    print(hj_1())
