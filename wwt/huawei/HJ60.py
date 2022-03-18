"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/24 下午5:37
@Site   : 
@File   : HJ60.py
@SoftWare: PyCharm
"""


def hj_60():
    num = int(input())
    store_list = []
    for i in range(2, num):
        if num % i == 0:
            continue
        else:
            store_list.append(i)
    print(store_list)


if __name__ == '__main__':
    hj_60()
