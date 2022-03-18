"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/17 上午8:58
@Site   : 
@File   : HJ8.py
@SoftWare: PyCharm
"""


def hj_8():
    num = int(input())
    store_dict = {}
    for _ in range(num):
        data = input().split(" ")
        if int(data[0]) in store_dict.keys():
            store_dict[int(data[0])] = store_dict[int(data[0])] + int(data[1])
        else:
            store_dict[int(data[0])] = int(data[1])

    for i in sorted(store_dict):
        print(i, store_dict[i])


if __name__ == '__main__':
    hj_8()
