"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/18 上午10:31
@Site   : 
@File   : HJ4.py
@SoftWare: PyCharm
"""


def hj_4():
    data = input()
    i = 0
    while True:
        if len(data[i * 8:]) > 8:
            print(data[i * 8: (i + 1) * 8])
            i += 1
            continue
        else:
            print(data[i * 8:] + (8 - len(data[i * 8:])) * "0")
            break


if __name__ == '__main__':
    hj_4()
