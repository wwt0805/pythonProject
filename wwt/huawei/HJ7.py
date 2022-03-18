"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/18 上午10:32
@Site   : 
@File   : HJ7.py
@SoftWare: PyCharm
"""


def hj_7():
    num = float(input())
    if num > 0:
        if num % 1 >= 0.5:
            print(int(num) + 1)
        else:
            print(int(num))


if __name__ == '__main__':
    hj_7()
