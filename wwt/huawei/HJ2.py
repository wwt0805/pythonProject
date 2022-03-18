"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/18 上午10:24
@Site   : 
@File   : HJ2.py
@SoftWare: PyCharm
"""


def hj_2():
    data = input().upper()
    sign = input()
    count = 0
    for _ in data:
        if _ == sign or _ == sign.upper():
            count += 1
    print(count)


if __name__ == '__main__':
    hj_2()
